from django.http import HttpResponse
from django.shortcuts import render

from add_task.models import TodoItem
from .forms import AddTodo

# Create your views here.
def addTask(request):
  if request.method == "POST":
    form = AddTodo(request.POST)
    form.save()
    todos = TodoItem.objects.all()
    stuff = {
       'tasks':todos
    }
    return render(request, 'home.html',context = stuff)
  else:
    form = AddTodo()
  data = {
    'myform': form
  }
  return render(request, 'add_task.html',context = data)

def edit_task(request,pk):
    print(pk)
    todos = TodoItem.objects.get(id = pk)
    form = AddTodo(instance=todos)
    if request.method == 'POST':
      form.save()
      todos = TodoItem.objects.all()
      stuff = {
        'tasks':todos
      }
      return render(request, 'home.html',context = stuff)
    data = {
    'myform': form
    }
    return render(request, 'edit_task.html',context=data)