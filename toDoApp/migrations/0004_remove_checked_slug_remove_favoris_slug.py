# Generated by Django 4.0.5 on 2022-06-19 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toDoApp', '0003_checked_remove_todomodel_checked_todomodel_checked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checked',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='favoris',
            name='slug',
        ),
    ]