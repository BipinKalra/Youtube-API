from django.shortcuts import render
from youtube.models import Video
from api.serializer import *
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from api.utils.pagination import Pagination

class VideoList(APIView):
  def get(self, request):
    offset = int(request.query_params.get('offset', 0))
    limit = int(request.query_params.get('limit', 10))
    
    videos = Video.objects.order_by('-published_at')[offset:offset+limit]
    pagination = Pagination(next_offset=offset+limit, limit=limit)

    serializer = PaginatedVideoSerializer({
      "videos": videos,
      "pagination": pagination
    })

    return Response(serializer.data)


class SearchList(generics.ListAPIView):
  # this searches using search query param
  queryset = Video.objects.order_by('-published_at')
  serializer_class = VideoSerializer
  filter_backends = [filters.SearchFilter]

  # Dollar sign forces regex match
  search_fields = ["$title", "$description"]
