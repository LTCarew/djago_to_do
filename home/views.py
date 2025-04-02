from django.http import HttpResponse
from django.shortcuts import render
from add_task .models import TodoItem
from django.views.generic import ListView

# Create your views here.
def home(request):
    todos = TodoItem.objects.all()
    stuff = {
       'tasks':todos
    }
    return render(request, template_name='home.html' ,context = stuff)






# class home(ListView):
#     template_name = 'home.html'
#     model=TodoItem
#     context_object_name = 'tasks'