from django.shortcuts import render,redirect
from .forms import RegisterUser
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'home.html')

def register_user(request):
    if request.method=='POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'You have successfully registered')
            return redirect('login')
    else:
        form = RegisterUser()
    return render(request,'register.html',{'form':form,'Title':'Register Page'})

@login_required
def profile(request):
    return render(request,'profile.html')

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user =  authenticate(username=name,password=user_pass)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged In Successfully')
                return redirect('profile')
            else:
                return redirect('register')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'Title':'Login','form':form,'button':'Login'})

@login_required
def logout_user(request):
        logout(request)
        messages.success(request,'Logged Out Successfully')
        return redirect('login')

@login_required
def withPass(request):
    if request.method=='POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password Changed Successfully')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'login.html',{'form':form,'Title':'Password Changed Form With Password','button':'Change Password'})
        
@login_required
def withoutPass(request):
    if request.method=='POST':
        form = SetPasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password Changed Successfully')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request,'login.html',{'form':form,'Title':'Password Changed Form Without Password','button':'Change Password'})