from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import AddTaskForm
from .models import Task

# Create your views here.


def task(request):
    num_tasks = Task.objects.count()
    tasks = Task.objects.all()
    return render(
        request,
        'templates/base.html',
        {'num_tasks': num_tasks, 'tasks': tasks},
    )


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
    return render(request, 'template/add.html', dict(form=form))
