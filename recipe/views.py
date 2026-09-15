from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Recipe
from rest_framework import serializers
from rest_framework.response import Response
from recipe.serializers import RecipeSerializer

@api_view(['GET','POST'])
def get_recipe(request):
    if request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        check = serializer.is_valid()
        if check == True:
            serializer.validated_data
            serializer.save()
        else:
            return Response(serializer.errors,status=400)
        return Response(serializer.data,status=201)
    else:
        recipe = Recipe.objects.all()
        serializer = RecipeSerializer(recipe,many=True)
        serializer.data
        return Response(serializer.data)
