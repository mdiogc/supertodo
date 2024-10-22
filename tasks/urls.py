from django.urls import path

from . import views

app_name = 'tasks'  # Namespaces the URLs for this app

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('<slug:task_slug>/', views.task_detail, name='task_detail'),
    path('<slug:task_slug>/edit/', views.edit_task, name='edit_task'),
    path('<slug:task_slug>/delete/', views.delete_task, name='delete_task'),
    path('<slug:task_slug>/toggle/', views.toggle_task, name='toggle_task'),
]
