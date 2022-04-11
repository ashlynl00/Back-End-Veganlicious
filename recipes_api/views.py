from django.shortcuts import render
from rest_framework import generics
from .serializers import RecipesSerializer
from .models import Recipes

# Create your views here.

class RecipesList(generics.ListCreateAPIView):
    queryset = Recipes.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = RecipesSerializer # tell django what serializer to use

class RecipesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipes.objects.all().order_by('id')
    serializer_class = RecipesSerializer
