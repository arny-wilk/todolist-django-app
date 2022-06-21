from django import forms
from .models import TodoModel


class TodoForm(forms.Form):
    text = forms.CharField(max_length=100
                           , widget=forms.TextInput(
            attrs={'type': 'text', 'placeholder': 'Ajouter ici votre tâche', 'name': 'content', 'id': 'content'}))

    class Meta:
        model = TodoModel
        fields = ['task', 'category']
