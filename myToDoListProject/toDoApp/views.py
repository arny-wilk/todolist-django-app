from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET

# Create your views here.
from toDoApp.forms import TodoForm, SignupForm
from toDoApp.models import TodoModel, Category


def signupage(request):

    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            print(signup_form.cleaned_data)
            return redirect("index")

    form = SignupForm()

    return render(request, "toDoApp/signupage.html", {"form": form})


def index(request):
    todo_list = TodoModel.objects.order_by('id')
    form = TodoForm()
    context = {"todo_list": todo_list, "form": form}
    return render(request, 'toDoApp/index.html', context)


@require_POST
def add_todo(request):
    form = TodoForm(request.POST)

    print(form)

    if form.is_valid():
        # new_todo = TodoModel(task=form.cleaned_data['task'])
        # new_todo.save()
        form.save()

    return redirect('index')


def update_todo(request, pk):
    task = TodoModel.objects.get(id=pk)

    form = TodoForm(instance=task)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'toDoApp/update_task.html', {'update_todo': form})


def favoris_todo(request):
    todo_to_favoris = TodoModel.objects.filter(favoris=False)
    todo_to_favoris.favoris = True
    todo_to_favoris.save()

    return redirect('index')


def delete_complete(request):
    TodoModel.objects.filter(checked=True).delete()

    return redirect('index')


def delete_all(request):
    TodoModel.objects.all().delete()

    return redirect('index')
