from django.db import models

# Create your models here.
class Recipes(models.Model):
    name = models.CharField(max_length=32)
    link = models.URLField(max_length=200)
    # directions = ArrayField(models.CharField(max_length=50))
    # ingredients = ArrayField(models.CharField(max_length=50))