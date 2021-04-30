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