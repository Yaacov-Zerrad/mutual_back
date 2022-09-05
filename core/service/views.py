from django.shortcuts import render
from rest_framework import generics, status, permissions
from service.models import CategoryService, Service
from .serializer import CategoryServiceSerializer, ServiceSerializer
from rest_framework.response import Response
from django.views import View

class AllServiceView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class LatestServiceView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    def get_queryset(self):
        return super().get_queryset()[0:8]



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