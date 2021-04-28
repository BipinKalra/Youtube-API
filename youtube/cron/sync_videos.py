import sys, os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "youtube_videos.settings")
django.setup()
from youtube.synchronizer import get_youtube_synchronizer
from django.conf import settings

if __name__ == "__main__":
  get_youtube_synchronizer().sync_videos()

