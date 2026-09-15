from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Recipe
from rest_framework import serializers
from rest_framework.response import Response
from recipe.serializers import RecipeSerializer

@api_view(['GET'])
def get_recipe(request):
    recipe = Recipe.objects.all()
    serializer = RecipeSerializer(recipe,many=True)
    serializer.data
    return Response(serializer.data)
