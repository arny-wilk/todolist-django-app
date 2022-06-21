from django import forms
from django.template.defaultfilters import slugify

from toDoApp.models import Category


class TodoForm(forms.Form):
    text = forms.CharField(max_length=100
                           , widget=forms.TextInput(
            attrs={'type': 'text', 'placeholder': 'Ajouter ici votre tâche', 'name': 'content', 'id': 'content'}))


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']

    name = forms.CharField()
    slug = forms.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)

        super().save(*args, **kwargs)

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple
    )
