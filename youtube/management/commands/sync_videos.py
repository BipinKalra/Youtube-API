'''
Created a command which runs a cronjob while having the scope for this repository as manage.py contains that information already.
Thus, a manage.py command is created which is called by crontab to sync youtube videos
'''

from django.core.management.base import BaseCommand, CommandError
from youtube.synchronizer import get_youtube_synchronizer

class Command(BaseCommand):
  help = 'Syncs Youtube Videos'

  def handle(self, *args, **options):
    get_youtube_synchronizer().sync_videos()