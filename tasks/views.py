from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Task

def create_task(request):
    description = request.POST.get('description')
    task = Task.objects.create(description=description)
    tasks = Task.objects.all()
    return render(request, 'tasks_list.html', {'tasks': tasks})

def display_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'display_tasks.html', {'tasks': tasks})

@require_http_methods(['DELETE'])
def delete_task(request, id):
    Task.objects.filter(id=id).delete()
    tasks = Task.objects.all()
    return render(request, 'tasks_list.html', {'tasks': tasks})
