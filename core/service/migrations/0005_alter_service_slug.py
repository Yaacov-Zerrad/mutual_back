# Generated by Django 4.1 on 2022-09-04 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_service_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(auto_created=True, unique=True),
        ),
    ]
