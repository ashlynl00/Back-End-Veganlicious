from django.shortcuts import render
from rest_framework import generics
from .serializers import RecipesSerializer
from .models import Recipes


from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class RecipesList(generics.ListCreateAPIView):
    queryset = Recipes.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = RecipesSerializer # tell django what serializer to use

class RecipesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipes.objects.all().order_by('id')
    serializer_class = RecipesSerializer

class ItemView(APIView):
    parser_classes = (MultiPartParser, FormParser)