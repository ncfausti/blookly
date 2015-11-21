from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name="stories")
    pub_date = models.DateTimeField('date published', null=True)
    content = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)