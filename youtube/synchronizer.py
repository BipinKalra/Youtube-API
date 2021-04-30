'''
YoutubeSynchronizer has a sync videos function which performs the fetch operation from exAPI thrice (capped currently, can be increased accroding to needs later).
These responses are appended to a list, followed by conversion of each element into a dictionary before bulk addition to the DB.
Herein, I have used bulk_update_or_create to perform an upsert function instead of a complete update/create.
'''

from youtube.models import Video
from youtube.services.exapi import get_youtube_exapi
from bulk_update_or_create import BulkUpdateOrCreateQuerySet

class YoutubeSynchronizer():
  def __init__(self, youtube_exapi):
    self._youtube_exapi = youtube_exapi

  def sync_videos(self):
    current_page = None

    videos = []

    for i in range(3):
      result, next_page_token = self._youtube_exapi.fetch_videos(current_page)
      videos += result
      current_page = next_page_token

    update_fields = [
      "title",
      "url",
      "thumbnail",
      "duration",
      "description",
      "published_at"
    ]
    videos = [Video.from_dict(video) for video in videos]
    
    Video.objects.bulk_update_or_create(videos, update_fields,match_field="video_id")
  

def get_youtube_synchronizer():
  return YoutubeSynchronizer(youtube_exapi=get_youtube_exapi())