from django.urls import path
from .views import index, add_todo

urlpatterns = [
    path('', index, name='index'),
    path('add', add_todo, name='add'),
]
