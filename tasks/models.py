from datetime import datetime

from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    slug = models.SlugField(unique=True, blank=True)
    complete_before = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
