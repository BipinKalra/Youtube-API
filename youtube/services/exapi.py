'''
Class YoutubeExApi is named such since this works with an external API to fetch content.
The class has two functions, one of which is private since its only called within the public function.
The private function _fetch_video_ids gets a list of video ids from the response of the request for a given search query.
The public function fetch_videos takes that result and fetches the corresponding videos and returns a list of videos along with the next page token.
'''

import requests
from isodate import parse_duration
from django.conf import settings

class YoutubeExApi:
  def __init__(self, api_url, api_key):
    self._api_url = api_url
    self._api_key = api_key

  def fetch_videos(self, page = None):
    ids, next_page_token = self._fetch_video_ids(page)

    params = {
      "part": "snippet,contentDetails",
      "key": self._api_key,
      "id": ",".join(ids),
      "max_results": 10,
    }

    response = requests.get(f"{self._api_url}/youtube/v3/videos", params=params)

    results = response.json()["items"]

    videos = [
      {
        "title" : video["snippet"]["title"],
        "url" : "https://www.youtube.com/watch?v=" + video["id"],
        "duration" : int(parse_duration(video["contentDetails"]["duration"]).total_seconds() // 60),
        "thumbnail" : video["snippet"]["thumbnails"]["high"]["url"],
        "description": video["snippet"]["description"],
        "id": video["id"],
        "publishedAt": video["snippet"]["publishedAt"]
      } 
      for video in results
    ]

    return videos, next_page_token

  
  def _fetch_video_ids(self, page):
    params = {
      "part": "snippet",
      "q": "golden state warriors",
      "key": self._api_key,
      "max_results": 10,
      "type": "video",
      "pageToken": page or ""
    }

    r = requests.get(f"{self._api_url}/youtube/v3/search", params=params)

    results = r.json()["items"]
    next_page_token = r.json()["nextPageToken"]

    videos = [video["id"]["videoId"] for video in results]

    return videos, next_page_token


def get_youtube_exapi():
  return YoutubeExApi(api_url = "https://www.googleapis.com", api_key = settings.YOUTUBE_DATA_API_KEY)