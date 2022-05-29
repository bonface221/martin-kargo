from django.db import models
from django.utils import timezone
from django_resized import ResizedImageField
from django.template.defaultfilters import slugify
from uuid import uuid4
from django.urls import reverse

import os
import json

# Create your models here.

class Category(models.Model):
  title = models.CharField(null=True, blank=True, max_length=180)

  #utility variable
  uniqueId = models.CharField(null=True, blank=True, max_length=100)
  slug = models.SlugField(max_length=500, blank=True, null=True, unique=True)
  date_created = models.DateTimeField(blank=True, null=True)
  last_updated = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return '{} {}'.format(self.title, self.uniqueId)

  def get_absolute_url(self):
    return reverse('category-detail', kwargs={'slug': self.slug})

  def save(self, *args, **kwargs):
    if self.date_created is None:
      self.date_created = timezone.localtime(timezone.now())
    if self.uniqueId is None:
      self.uniqueId = str(uuid4()).split('-')[4]
      self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
