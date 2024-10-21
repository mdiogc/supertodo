from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('add-task/', views.add_task, name='add-task'),
    path('tasks/<task_slug>', views.task_detail, name='task-detail'),
]
