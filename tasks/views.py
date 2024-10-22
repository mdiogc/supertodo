from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import AddTaskForm
from .models import Task


def task_list(request: HttpRequest) -> HttpResponse:
    show_completed = request.GET.get('show_completed', 'all')

    # Obtener todas las tareas
    all_tasks = Task.objects.all().order_by('done', 'complete_before')
    
    if show_completed == 'true':
        completed_tasks = all_tasks.filter(done=True)
        incomplete_tasks = []
    elif show_completed == 'false':
        completed_tasks = []
        incomplete_tasks = all_tasks.filter(done=False)
    else:  # 'all'
        completed_tasks = all_tasks.filter(done=True)
        incomplete_tasks = all_tasks.filter(done=False)

    return render(
        request,
        'tasks/task-list.html',
        {
            'incomplete_tasks': incomplete_tasks,
            'completed_tasks': completed_tasks,
            'show_completed': show_completed,
        },
    )





def task_detail(request: HttpRequest, task_slug: str) -> HttpResponse:
    task = Task.objects.filter(slug=task_slug).first()
    if task is None:
        return render(request, 'tasks/task-detail.html', {'error': 'Task not found'})
    return render(request, 'tasks/task-detail.html', {'task': task})


def add_task(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = AddTaskForm()
    else:
        form = AddTaskForm(data=request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            return redirect('tasks:task-list')
    return render(request, 'tasks/add-task.html', {'form': form})


def edit_task(request: HttpRequest, task_slug: str) -> HttpResponse:
    task = Task.objects.filter(slug=task_slug).first()
    if task is None:
        return HttpResponse('Task not found', status=404)

    if request.method == 'POST':
        form = AddTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:task-detail', task_slug=task.slug)
    else:
        form = AddTaskForm(instance=task)

    return render(request, 'tasks/edit-task.html', {'form': form, 'task': task})


def delete_task(request: HttpRequest, task_slug: str) -> HttpResponse:
    task = Task.objects.filter(slug=task_slug).first()
    if task is None:
        return HttpResponse('Task not found', status=404)

    if request.method == 'POST':
        task.delete()
        return redirect('tasks:task-list')

    return render(request, 'tasks/delete-task.html', {'task': task})


def toggle_task(request: HttpRequest, task_slug: str) -> HttpResponse:
    task = Task.objects.filter(slug=task_slug).first()
    if task is None:
        return HttpResponse('Task not found', status=404)
    task.done = not task.done
    task.save()
    return redirect('tasks:task-list')



