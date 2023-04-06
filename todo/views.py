from django.shortcuts import render
from .models import Todo
from .forms import MyForm
from django.http import HttpResponseRedirect
# Create your views here.


def todo(request):
    todos = Todo.objects.all()
    template = 'todo/todo.html'
    context = {
        'todos': todos
    }
    return render(request, template, context)


def createtodo(request):
    x = request.POST['task']
    new_item = Todo(task=x)
    new_item.save()
    return HttpResponseRedirect('/todo/')

def removetodo(request, i):
    y = Todo.objects.get(id = i)
    y.delete()
    return HttpResponseRedirect('/todo/')
