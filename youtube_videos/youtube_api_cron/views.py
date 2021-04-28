import requests
from isodate import parse_duration

from django.conf import settings
from django.shortcuts import render

# Create your views here.

def index(request):
  search_url = "https://www.googleapis.com/youtube/v3/search"
  video_url= "https://www.googleapis.com/youtube/v3/videos"

  search_params = {
    "part": "snippet",
    "q": "golden state warriors",
    "key": settings.YOUTUBE_DATA_API_KEY,
    "max_results": 9,
    "type": "video"
  }

  video_ids = []
  r = requests.get(search_url, params=search_params)

  results = r.json()["items"]

  for result in results:
    video_ids.append(result["id"]["videoId"])
  
  video_params = {
    "part": "snippet,contentDetails",
    "key": settings.YOUTUBE_DATA_API_KEY,
    "id": ",".join(video_ids)
  }

  v = requests.get(video_url, params=video_params)

  video_results = v.json()["items"]

  videos = []

  for result in video_results:
    video = {
    "title" : result["snippet"]["title"],
    "id" : result["id"],
    "duration" : parse_duration(result["contentDetails"]["duration"]).total_seconds() // 60,
    "thumbnail" : result["snippet"]["thumbnails"]["high"]["url"],
    }

    videos.append(video)

  print(videos)

  return render(request, "search/index.html")