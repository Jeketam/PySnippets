from django.shortcuts import render
from .models import Task


def task_list(request):
    tasks = Task.published.all()
    return render(request, 'blog/task/list.html', {'tasks': tasks})
