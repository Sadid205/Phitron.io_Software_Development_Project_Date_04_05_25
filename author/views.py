from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,"Account created successfully.")
            form.save()
            return redirect('login')
    else:
        form = forms.UserRegistrationForm()
    return render(request,'register.html',{"form":form,"Title":"Register Page"})

class user_login(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self,form):
        messages.success(self.request,'Logged in successfully')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.success(self.request,"Logged in information incorrect.Please try again.")
        return super().form_invalid(form)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        
        context['Title'] = "Login Page"

        return context
