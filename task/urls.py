from django.contrib import admin
from django.urls import include, path
from venv import create
from .views import CreateTask,DeleteTask,UpdateTask,TaskDetail
from task import views

urlpatterns = [
    
    path('add/',CreateTask.as_view()),
    path('view/',views.index),
    path('<pk>/delete/', DeleteTask.as_view()),
    path('<pk>/update/', UpdateTask.as_view()),
    path('<pk>/view/', TaskDetail.as_view()),
]