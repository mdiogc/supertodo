from django.shortcuts import render

from .models import Task

# Create your views here.


def task(request):
    num_tasks = Task.objects.count()
    tasks = Task.objects.all()
    return render(
        request,
        'tasks/base.html',
        {'num_tasks': num_tasks, 'tasks': tasks},
    )


def task_detail(request, post_slug: str):
    task = Task.objects.get(slug=post_slug)
    return render(request, 'tasks/detail.html', dict(task=task))
