from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import AddTaskForm
from .models import Task

# Create your views here.


def task_list(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    return render(request, 'tasks/task-list.html', dict(task=tasks))


def task_detail(request, task_slug: str):
    task = Task.objects.get(slug=task_slug)
    return render(request, 'tasks/detail.html', dict(task=task))


def add_task(request):
    if request.method == 'GET':
        form = AddTaskForm()
    else:
        if (form := AddTaskForm(data=request.Task)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            return redirect('task:task')
    return render(request, 'templates/add-task.html', dict(form=form))
