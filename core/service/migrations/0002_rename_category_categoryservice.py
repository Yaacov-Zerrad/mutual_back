# Generated by Django 4.1 on 2022-09-04 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='CategoryService',
        ),
    ]