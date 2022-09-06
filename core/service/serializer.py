from dataclasses import field, fields
from rest_framework import serializers
from .models import Service, CategoryService


class CategoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryService
        fields =['name', 'slug']

class ServiceSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    class Meta: 
        model = Service 
        fields = ['category', 'title', 'description', 'date_add', 'get_absolute_url', 'position']



class CategoryServiceSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(many=True)
    
    class Meta:
        model = CategoryService
        fields = '__all__'
 

