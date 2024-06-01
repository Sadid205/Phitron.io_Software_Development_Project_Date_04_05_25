from django.shortcuts import render
from TaskModel.models import TaskModel

def Home(request):
    Tasks = TaskModel.objects.all()
    # for Task in Tasks:
    #    print(Task.TaskTitle)
    #    for category in Task.Category.all():
    #        print(category.CategoryName)
    return render(request,'home.html',{"Tasks":Tasks})

