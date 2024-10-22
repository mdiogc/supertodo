from django.urls import path

from . import views

app_name = 'tasks'  # Namespaces the URLs for this app

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('add/', views.add_task, name='add-task'),
    path('<slug:task_slug>/', views.task_detail, name='task-detail'),
    path('<slug:task_slug>/edit/', views.edit_task, name='edit-task'),
    path('<slug:task_slug>/delete/', views.delete_task, name='delete-task'),
    path('<slug:task_slug>/toggle/', views.toggle_task, name='toggle-task'),
]
