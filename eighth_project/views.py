from django.shortcuts import render
from first_app.forms import RegisterForm
def Signup(request):
    form = RegisterForm()
    return render(request,'signup.html',{'form':form})