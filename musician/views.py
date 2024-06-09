from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from .models import musician
from .forms import musician_form
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required,name='dispatch')
class add_musician(CreateView):
    model = musician
    form_class = musician_form
    template_name = "add_musician.html"
    success_url = reverse_lazy('homepage')

    def form_valid(self,form):
        form.save()
        messages.success(self.request,"You have successfully created a musician")
        return super().form_valid(form)

    def get_context_data(self,**kwargs):
        context =  super().get_context_data(**kwargs)
        context['Title'] = "Add Musician"
        return context

@method_decorator(login_required,name='dispatch')
class edit_musician(UpdateView):
    model = musician
    form_class = musician_form
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

    def form_valid(self,form):
        form.save()
        messages.success(self.request,"You have successfully updated an album")
        return super().form_valid(form)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context ['Title'] = "Edit Musician"
        return context


