# Generated by Django 4.1 on 2022-09-04 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_alter_service_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='slug',
        ),
    ]
