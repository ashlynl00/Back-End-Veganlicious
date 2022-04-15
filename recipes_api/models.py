from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Recipes(models.Model):
    name = models.CharField(max_length=32)
    link = models.URLField(max_length=200)
    image = models.CharField(max_length=2000, default='https://i.imgur.com/BSnwSzw.png', null=True, blank=True)
    description = models.CharField(max_length=350, null=True, blank=True)
    directions = models.CharField(max_length=750, null=True, blank=True)
    ingredients = models.CharField(max_length=250, null=True, blank=True)
    tags = models.CharField(max_length=20, null=True, blank=True)