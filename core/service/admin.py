from django.contrib import admin

from .models import CategoryService, Service

admin.site.register(Service)
admin.site.register(CategoryService)
