from django.db import models

class Video(models.Model):
  title = models.CharField(max_length=500)
  url = models.URLField(max_length=500)
  thumbnail = models.URLField(max_length=500)
  duration = models.IntegerField()

  def __str__(self):
    return self.title
