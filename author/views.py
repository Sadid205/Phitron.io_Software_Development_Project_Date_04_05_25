from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import UserOrder
from car.models import Car
from author.models import UserOrder
from .forms import EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.

def UserSignUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request,'SignUp.html',{"form":form,"title":"Sign Up Form","buttonName":"Sign Up"})


class UserLogin(LoginView):
    template_name = 'Login.html'

    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self,form):
        messages.success(self.request,"You have successfully logged in")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.success(self.request,"Incorrect username or password")
        return super().form_invalid(form)
    
    def get_context_data(self,**kwargs):
        
        context = super().get_context_data(**kwargs)
        context['title'] = "Login Form"
        context['buttonName'] = "Login"

        return context
    
@login_required
def Profile(request):
    orders = UserOrder.objects.filter(user=request.user)
    return render(request,'Profile.html',{"orders":orders})

@login_required
def EditProfile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            messages.success(request,"You have successfully updated your profile")
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request,'SignUp.html',{'form':form,"title":"Edit Profile Form","buttonName":"Update"})

@login_required
def Buy(request,id):
    user = request.user
    car = Car.objects.get(id=id)
    try:
        ExistingOrder = UserOrder.objects.get(user=user,car=car)
        isFound = True
    except:
        ExistingOrder = None
        isFound = False
        
    if car.quantity>0:
        car.quantity-=1
        car.save()
    else:
        messages.warning(request,"This car is not available at this moment")
        return render(request,'CarDetails.html',{"title":"Car Details Page","car":car})
    if isFound==True:
            ExistingOrder.quantity+=1
            ExistingOrder.save()
            messages.success(request,"You have successfully placed and order.")  
    else:
        newOrder = UserOrder()
        newOrder.user = user
        newOrder.car = car
        newOrder.quantity = 1
        newOrder.save()
        messages.success(request,"You have successfully placed and order.")

    return redirect("profile")

@login_required
def ChangePassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,request.user)
                messages.success(request,"You have successfully updated your password")
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'ChangePass.html',{"form":form,"title":"Password Change Form","buttonName":"Update Password"})
    else:
        return redirect('login')
