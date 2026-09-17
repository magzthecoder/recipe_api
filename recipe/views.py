from rest_framework.decorators import api_view, permission_classes
from .models import Recipe
from rest_framework.response import Response
from recipe.serializers import RecipeSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def favourite_recipe(request,id):
    recipe = get_object_or_404(Recipe,id=id)
    if request.method == 'POST':
        if recipe.favourited_by.filter(id=request.user.id).exists(): #checks if user and recipe model have a relationship
            return Response('No duplicates',status=400)
        else:
            recipe.favourited_by.add(request.user)
            return Response(status=201)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def un_favourite_recipe(request,id):
    if request.method == 'DELETE':
        recipe = get_object_or_404(Recipe,id=id)
        if recipe.favourited_by.filter(id=request.user.id).exists(): 
            recipe.favourited_by.remove(request.user)
            return Response(status=204)
        else:
            return Response('Not favoured yet',status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_favourites(request):
    recipes = Recipe.objects.filter(favourited_by=request.user)
    if recipes.exists():
        serializer = RecipeSerializer(recipes,many=True)
        return Response(serializer.data,status=200)
    else:
        serializer = RecipeSerializer(recipes,many=True)
        return Response(serializer.data,status=200)
