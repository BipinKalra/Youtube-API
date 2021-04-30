from rest_framework import serializers
from youtube.models import Video

class VideoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Video
    fields = ["video_id","title","url","thumbnail","duration","description", "published_at"]

class PaginationSerializer(serializers.Serializer):
  next_offset = serializers.IntegerField()
  limit = serializers.IntegerField()

class PaginatedVideoSerializer(serializers.Serializer):
  videos = VideoSerializer(many=True, read_only=True)
  pagination = PaginationSerializer(read_only=True)