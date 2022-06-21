from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    category_name = models.CharField(max_length=36)
    slug = models.SlugField()

    class Meta:
        verbose_name = "Catégorie"

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)

        super().save(*args, **kwargs)


class Checked(models.Model):
    checked = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Tâches terminées"

    def __str__(self):
        return "(vide)" if self.checked else "Coché"


class Favoris(models.Model):
    favoris = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Tâches favorites"

    def __str__(self):
        return "(vide)" if self.favoris else "Favoris"


class TodoModel(models.Model):
    category = models.ManyToManyField(Category)
    checked = models.ManyToManyField(Checked, blank=True)
    favoris = models.ManyToManyField(Favoris, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    task = models.CharField(max_length=100)
    slug = models.SlugField()
    date = models.DateField(blank=True, null=True)
    task_details = models.TextField(blank=True)

    class Meta:
        verbose_name = "Tâche"
        ordering = ["date"]

    def __str__(self):
        return self.task

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.task)

        super().save(*args, **kwargs)