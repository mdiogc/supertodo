from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils.text import slugify
from .forms import AddTaskForm
from .models import Task

# Task list view
def task_list(request: HttpRequest) -> HttpResponse:
    show_completed = request.GET.get('show_completed', 'false') == 'true'
    
    if show_completed:
        incomplete_tasks = []
        completed_tasks = Task.objects.filter(done=True).order_by('updated_at')
    else:
        incomplete_tasks = Task.objects.filter(done=False).order_by('complete_before')
        completed_tasks = []

    return render(request, 'tasks/task-list.html', {
        'incomplete_tasks': incomplete_tasks,
        'completed_tasks': completed_tasks,
        'show_completed': show_completed,
    })
# Task detail view
def task_detail(request: HttpRequest, task_slug: str) -> HttpResponse:
    task = Task.objects.filter(slug=task_slug).first()  # Using filter().first() to get the task
    if task is None:
        return render(request, 'tasks/task-detail.html', {'error': 'Task not found'})  # Render an error message if the task is not found
    return render(request, 'tasks/task-detail.html', {'task': task})

# Add task view
def add_task(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = AddTaskForm()
    else:
        form = AddTaskForm(data=request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)  # Create a slug from the task name
            task.save()  # Save the task to the database
            return redirect('tasks:task_list')  # Redirect to the task list view after adding the task
    return render(request, 'tasks/add-task.html', {'form': form})

# Edit task view
def edit_task(request: HttpRequest, task_slug: str) -> HttpResponse:
    task = Task.objects.filter(slug=task_slug).first()  # Using filter().first() instead of get()
    if task is None:
        return HttpResponse("Task not found", status=404)  # Handle the case where the task does not exist

    if request.method == 'POST':
        form = AddTaskForm(request.POST, instance=task)  # Populate the form with the existing task data
        if form.is_valid():
            form.save()  # Save the updated task to the database
            return redirect('tasks:task_detail', task_slug=task.slug)  # Redirect to the task detail view
    else:
        form = AddTaskForm(instance=task)  # Pre-fill the form with the current task data

    return render(request, 'tasks/edit-task.html', {'form': form, 'task': task})

# Delete task view
def delete_task(request: HttpRequest, task_slug: str) -> HttpResponse:
    task = Task.objects.filter(slug=task_slug).first()  # Using filter().first() instead of get()
    if task is None:
        return HttpResponse("Task not found", status=404)  # Handle the case where the task does not exist

    if request.method == 'POST':
        task.delete()  # Delete the task
        return redirect('tasks:task_list')  # Redirect to the task list view after deletion

    return render(request, 'tasks/delete-task.html', {'task': task})  # Render a confirmation page for deletion

# Toggle task completion view
def toggle_task(request: HttpRequest, task_slug: str) -> HttpResponse:
    task = Task.objects.filter(slug=task_slug).first()  # Using filter().first() instead of get()
    if task is None:
        return HttpResponse("Task not found", status=404)  # Handle the case where the task does not exist

    task.done = not task.done  # Toggle the task's completion status
    task.save()  # Save the updated task
    return redirect('tasks:task_list')  # Redirect to the task list view
