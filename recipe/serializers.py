from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['name','description','price']

    def validate_price(self,price):
        if price > 0:
            return price
        else:
            raise serializers.ValidationError("Price should be positive")

    def validate(self,data):
        if data.get('name',self.instance.name) == data['description']:
            raise serializers.ValidationError("Name and Description cannot be the same")
        else:
            return data

    def create(self, validated_data):
        validated_data['description'] = "Recipe: " + validated_data['description']
        return Recipe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = "Updated: " + validated_data.get('description', instance.description)
        instance.save()
        return instance