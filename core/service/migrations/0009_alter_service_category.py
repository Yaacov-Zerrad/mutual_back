# Generated by Django 4.1 on 2022-09-04 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_remove_service_category_service_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ManyToManyField(default='other', related_name='prod', to='service.categoryservice'),
        ),
    ]
