from rest_framework import serializers
from youtube.models import Video

class VideoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Video
    fields = ["video_id","title","url","thumbnail","duration","description"]