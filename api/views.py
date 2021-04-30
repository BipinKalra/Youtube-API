from django.shortcuts import render
from youtube.models import Video
from api.serializer import *
from rest_framework import generics, filters

class VideoList(generics.ListAPIView):
  def get_queryset(self):
    offset = request.query_params.get('offset')
    limit = request.query_params.get('limit')

    if not (not offset and not limit):
      return []
    
    return Video.objects.all()

  serializer_class = VideoSerializer


class SearchList(generics.ListAPIView):
  # this searches using search query param
  queryset = Video.objects.all()
  serializer_class = VideoSerializer
  filter_backends = [filters.SearchFilter]

  # Dollar sign forces regex match
  search_fields = ["$title", "$description"]
