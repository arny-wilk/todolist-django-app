from django.urls import path
from .views import index, add_todo, signupage, update_todo, favoris_todo, delete_complete, delete_all

urlpatterns = [
    path('signupage/', signupage, name='signupage'),
    path('', index, name='index'),
    path('add', add_todo, name='add'),
    path('update_todo/<int:pk>/', update_todo, name='update_todo'),
    path('favoris_todo', favoris_todo, name='favoris_todo'),
    path('delete_complete', delete_complete, name='delete_complete'),
    path('delete_all', delete_all, name='delete_all')
]
