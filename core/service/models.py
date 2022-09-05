from django.db import models


class CategoryService(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name



class Service(models.Model):
    category = models.ManyToManyField(CategoryService, related_name='prod')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=True)

    class Meta:
        ordering = ('-date_add',)

    def __str__(self):
        return self.title

    def slug(self):
        return self.pk
    