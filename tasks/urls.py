from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task, name='task'),
    path('post/add/', views.add_task, name='add-task'),
    path('tasks/<task_slug>', views.task_detail, name='task-detail'),
]
