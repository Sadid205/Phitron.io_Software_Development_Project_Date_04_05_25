from django.shortcuts import render,redirect
from .forms import TaskModelForm
from .models import TaskModel
# Create your views here.

def AddTask(request):
    if request.method=="POST":
        Task = TaskModelForm(request.POST)
        if Task.is_valid():
            Task.save()
            return redirect("homepage")
    else:
        Task = TaskModelForm()
    return render(request,'AddTask.html',{"Form":Task,"Title":"Add Task"})


def EditTask(request,id):
    Task = TaskModel.objects.get(pk=id)
    TaskForm = TaskModelForm(instance=Task)
    if request.method=="POST":
        TaskForm = TaskModelForm(request.POST,instance=Task)
        if TaskForm.is_valid():
            TaskForm.save()
            return redirect("homepage")
    else:
        TaskForm = TaskModelForm(instance=Task)
    return render(request,'AddTask.html',{"Form":TaskForm,"Title":"Edit Task"})


def deleteTask(request,id):
    Task = TaskModel.objects.get(pk=id)
    Task.delete()
    return redirect('homepage')