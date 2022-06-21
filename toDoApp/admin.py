from django.contrib import admin

# Register your models here.
from toDoApp.models import TodoModel, Category

admin.site.register(TodoModel)
admin.site.register(Category)
