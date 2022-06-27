from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=36)
    slug = models.SlugField()

    class Meta:
        verbose_name = "Catégorie"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)


class TodoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    task = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    slug = models.SlugField()
    date = models.DateField(blank=True, null=True)
    checked = models.BooleanField(default=False)
    favoris = models.BooleanField(default=False)
    task_details = models.TextField(blank=True)

    class Meta:
        verbose_name = "Tâche"
        ordering = ["date"]

    def __str__(self):
        return {self.task}

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.task)

        super().save(*args, **kwargs)