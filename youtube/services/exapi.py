import requests
from isodate import parse_duration

class YoutubeExApi:
  def __init__(self, api_url, api_key):
    self._api_url = api_url
    self._api_key = api_key

  def fetch_videos(self, page = None):
    ids = self._fetch_video_ids(page)

    params = {
      "part": "snippet,contentDetails",
      "key": self._api_key,
      "id": ",".join(ids),
      "max_results": 10,
    }

    response = requests.get(f"{self._api_url}/youtube/v3/videos", params=params)

    results = response.json()["items"]

    return [
      {
        "title" : video["snippet"]["title"],
        "url" : "https://www.youtube.com/watch?v=" + video["id"],
        "duration" : int(parse_duration(video["contentDetails"]["duration"]).total_seconds() // 60),
        "thumbnail" : video["snippet"]["thumbnails"]["high"]["url"],
      } 
      for video in results
    ]

  
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

    return [video["id"]["videoId"] for video in results]