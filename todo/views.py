from django.shortcuts import redirect, render, redirect
from django.http import HttpResponse
from .models import TODOS
from .forms import ListForms
# Create your views here.

def index(request):

    todo_list = TODOS.objects.all() 
    return render(request, 'todo/index.html', {'todo_list': todo_list})

def about(requset):
    return render(requset, template_name='todo/about.html')

def create(requset):
    if requset.method == "POST":
        form = ListForms(requset.POST or None)

        if form.is_valid:
            form.save()
            todo_list = TODOS.objects.all()
            return render(requset, 'todo/create.html', {'todo_list': todo_list})
    else:
        todo_list = TODOS.objects.all() 
        return render(requset, 'todo/create.html', {'todo_list': todo_list})
    
def delete(request, TODOS_id):
    todo = TODOS.objects.get(pk=TODOS_id)
    todo.delete()

    return redirect("index")

def yes_finish(request, TODOS_id):
    todo = TODOS.objects.get(pk=TODOS_id)
    todo.is_finished = False
    todo.save()

    return redirect("index")

def no_finish(request, TODOS_id):
    todo = TODOS.objects.get(pk=TODOS_id)
    todo.is_finished = True
    todo.save()

    return redirect("index")

def update(request, TODOS_id):
    if request.method == "POST":
        todo_list = TODOS.objects.get(pk=TODOS_id)
        form = ListForms(request.POST or None, instance=todo_list)
        if form.is_valid:
            form.save()
            return redirect("index")
    else:
        todo_list = TODOS.objects.all() 
        return render(request, template_name='todo/update.html')