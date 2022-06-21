# Generated by Django 4.0.5 on 2022-06-19 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDoApp', '0005_remove_todomodel_checked_todomodel_checked_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=36)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Catégorie',
            },
        ),
        migrations.AddField(
            model_name='todomodel',
            name='category',
            field=models.ManyToManyField(to='toDoApp.category'),
        ),
    ]