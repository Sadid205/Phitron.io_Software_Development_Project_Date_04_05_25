from django.shortcuts import render,redirect
from .forms import TaskCategoryForm
# Create your views here.

def AddCategory(request):
    if request.method=="POST":
        Category = TaskCategoryForm(request.POST)
        if Category.is_valid():
            Category.save()
            return redirect('homepage')
    else:
        Category = TaskCategoryForm()
    return render(request,'AddCategory.html',{"Form":Category})