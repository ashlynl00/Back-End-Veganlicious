from rest_framework import serializers 
from .models import Recipes 

class RecipesSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Recipes # tell django which model to use
        fields = ('id', 'name', 'link', 'image', 'description', 'directions', 'ingredients', 'tags') # tell django which fields to include