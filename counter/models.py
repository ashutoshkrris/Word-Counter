from django.db import models
from picklefield.fields import PickledObjectField

# Create your models here.
class SiteList(models.Model):
    site_name = models.URLField(blank=False)
    result = PickledObjectField()
    location = models.CharField(max_length=255, default="Database")