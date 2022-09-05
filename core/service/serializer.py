from dataclasses import field, fields
from rest_framework import serializers
from .models import Service, CategoryService


class ServiceSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Service 
        fields = '__all__'



class CategoryServiceSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(many=True)
    
    class Meta:
        model = CategoryService
        fields = '__all__'


