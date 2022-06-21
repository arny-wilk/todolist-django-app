from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

# Create your views here.
from toDoApp.forms import TodoForm, CategoryForm
from toDoApp.models import TodoModel, Category, Checked, Favoris


def index(request):
    todo_list = TodoModel.objects.order_by('id')
    form = TodoForm()
    category = Category.objects.order_by('id')
    complete = Checked.objects.get(pk=1)
    todo_complete = complete.todomodel_set.all()
    favoris = Favoris.objects.get(pk=1)
    todo_favoris = favoris.todomodel_set.all()
    context = {"todo_list": todo_list, "form": form, "category": category, "todo_complete": todo_complete,
               "todo_favoris": todo_favoris}
    return render(request, 'toDoApp/index.html', context)


@require_POST
def add_todo(request):
    form = TodoForm(request.POST), CategoryForm(request.POST)

    if form[0].is_valid() and form[1].is_valid():
        new_todo = TodoModel(task=request.POST['text'], category=request.POST['category_name'])
        new_todo.save()

    return redirect('index')
