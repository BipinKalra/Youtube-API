from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path("videos", views.VideoList.as_view(), name="videos"),
  path("search", views.SearchList.as_view(), name="search"),
]