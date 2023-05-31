from rest_framework import serializers

from .models import Category, Food


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
