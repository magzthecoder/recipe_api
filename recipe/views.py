from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Recipe
from rest_framework.response import Response
from recipe.serializers import RecipeSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET','POST'])
def get_recipes(request):
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
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes,many=True)
        serializer.data
        return Response(serializer.data)

@api_view(['GET'])
def get_recipe(request,id):
    recipe = get_object_or_404(Recipe,id=id)
    serializer = RecipeSerializer(recipe)
    serializer.data
    return Response(serializer.data, status=200)
