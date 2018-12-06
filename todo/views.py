from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo


def todo(request):
    todos = Todo.objects

    return render(request, 'todo/todo.html',{'todo' : todo})
