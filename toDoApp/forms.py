from django import forms

from toDoApp.models import TodoModel, Category


class SignupForm(forms.Form):
    pseudo = forms.CharField(max_length=15, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    cgu_accept = forms.BooleanField(initial=True)

    def clean_pseudo(self):
        pseudo = self.cleaned_data.get("pseudo")
        if "$" in pseudo:
            raise forms.ValidationError("Le pseudo ne peut pas contenir de $.")
        return pseudo


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['task']
        widgets = {
            'task': forms.TextInput(
                attrs={'type': 'text', 'placeholder': 'Ajouter ici votre tâche', 'name': 'content', 'id': 'content'})
        }
        labels = {'task': ''}
        required = {'task': True}
        max_length = {'task': 225}


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']