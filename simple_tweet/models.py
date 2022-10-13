from django.db import models
from django.utils import timezone

class Texts(models.Model):

  user_name = models.CharField(max_length=50, null=False)
  text = models.CharField(max_length=50, null=False)
  created_at = models.DateTimeField()

  def save(self, *args, **kwargs):
    if not self.id:
      self.created_at = timezone.now()
    return super().save(*args, **kwargs)