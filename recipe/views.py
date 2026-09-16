from rest_framework.decorators import api_view
from .models import Recipe
from rest_framework.response import Response
from recipe.serializers import RecipeSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET','POST'])
def get_recipes(request): #get all recipes
    if request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        check = serializer.is_valid()
        if check == True:
            serializer.save()
        else:
            return Response(serializer.errors,status=400)
        return Response(serializer.data,status=201)
    else:
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_recipe(request,id): #get one recipe
    recipe = get_object_or_404(Recipe,id=id)
    serializer = RecipeSerializer(recipe)
    return Response(serializer.data, status=200)

@api_view(['GET','PUT'])
def update_recipe(request,id):#update one recipe
    recipe = get_object_or_404(Recipe,id=id)
    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=200)
    
    elif request.method == 'PUT':
        serializer = RecipeSerializer(recipe,data=request.data)
        check = serializer.is_valid()
        if check == True:
            serializer.save()
        else:
            return Response(serializer.errors,status=400)
        return Response(serializer.data,status=200)

@api_view(['GET','DELETE'])
def delete_recipe(request,id): #delete recipe
    recipe = get_object_or_404(Recipe,id=id)
    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=200)

    elif request.method == 'DELETE':
        recipe.delete()
        return Response(status=204)

@api_view(['GET','PATCH'])
def patch_recipe(request,id):#partially update a recipe
    recipe = get_object_or_404(Recipe,id=id)
    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=200)

    elif request.method == 'PATCH':
        serializer = RecipeSerializer(recipe, data=request.data,partial=True)
        check = serializer.is_valid()
        if check == True:
            serializer.save()
        else:
            return Response(serializer.errors,status=400)
        return Response(serializer.data,status=200)

