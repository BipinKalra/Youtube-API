# The from_dict function takes in a python object and returns an object of model class Video which is used before bulk create in the synchronizer

from django.db import models
from bulk_update_or_create import BulkUpdateOrCreateQuerySet

class Video(models.Model):
  objects = BulkUpdateOrCreateQuerySet.as_manager()

  video_id = models.CharField(primary_key=True, max_length=255)
  title = models.CharField(max_length=500)
  url = models.URLField()
  thumbnail = models.URLField()
  duration = models.IntegerField()
  description = models.TextField()
  published_at = models.DateTimeField()

  def __str__(self):
    return self.title

  @classmethod
  def from_dict(cls, dikt):
    return cls(
      video_id = dikt["id"],
      title = dikt["title"],
      url = dikt["url"],
      thumbnail = dikt["thumbnail"],
      duration = dikt["duration"],
      description = dikt["description"],
      published_at = dikt["publishedAt"]
    )
