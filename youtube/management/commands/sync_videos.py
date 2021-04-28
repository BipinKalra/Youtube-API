from django.core.management.base import BaseCommand, CommandError
from youtube.synchronizer import get_youtube_synchronizer

class Command(BaseCommand):
  help = 'Syncs Youtube Videos'

  def handle(self, *args, **options):
    get_youtube_synchronizer().sync_videos()