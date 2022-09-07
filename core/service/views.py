from django.shortcuts import render
from rest_framework import generics, status, permissions
from service.models import CategoryService, Service
from .serializer import CategoryNameSerializer, CategoryServiceSerializer, ServiceSerializer
from rest_framework.response import Response
from django.views import View
from rest_framework.views import APIView
from django.http import Http404




class AllServiceView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class CategoryServiceView(generics.ListAPIView):
    queryset = CategoryService.objects.all()
    serializer_class = CategoryNameSerializer
   

class OneCategoryServiceView(APIView):
    def get_object(self, category_slug):
        try:
            return CategoryService.objects.get(slug=category_slug)
        except Service.DoesNotExist:
            raise Http404
        
    def get(self, request, category_slug,  format=None):
        category = self.get_object(category_slug)
        category = Service.objects.filter(category=category)
        serializer = ServiceSerializer(category, many=True)
        return Response(serializer.data)



class LatestServiceView(APIView):
    def get(self, request, format=None):
        service = Service.objects.all()
        serializer = CategoryNameSerializer(service, many=True)
        return Response(serializer.data)



class DetailServiceView(generics.RetrieveAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()



class CreateServiceView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class UpdateServiceView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class DeleteServiceView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()