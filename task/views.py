from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .models import Task
from django.views.generic import DetailView
from django.http import request
# Create your views here.

class CreateTask(CreateView):
    model = Task
    fields = ['task_name', 'task_description']
    template_name = "task/create_task.html"
    success_url = '/task/view/'

class DeleteTask(DeleteView):
    model = Task
    template_name = "task/task_confirm_delete.html"
    success_url = 'task/view/'

def index(request):
    return render(request, 'Task/index.html') 

class UpdateTask(UpdateView):
    template_name = "task/update_task.html"
    model = Task
    fields = ['task_name', 'task_description']
    success_url = '/task/view/'   

class TaskDetail(DetailView):
    model = Task
    template_name = 'Task/task_detail.html'    