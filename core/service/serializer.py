from dataclasses import field, fields
from rest_framework import serializers
from .models import Service, CategoryService


class CategoryNameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CategoryService
        fields =['name', 'get_absolute_url']
        read_only_fields = fields

class ServiceSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.name')
    date_add = serializers.DateTimeField(format="%d/%m/%Y")
    class Meta: 
        model = Service 
        fields = [ 'title','description', 'date_add', 'get_absolute_url', 'position']



class CategoryServiceSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(many=True)
    
    class Meta:
        model = CategoryService
        fields = '__all__'
 

