from django.shortcuts import render

# Create your views here.

def first_app_home(request):
    return render(request,'first_app/home.html')

def contact(request):
    return render(request,'first_app/contact.html')