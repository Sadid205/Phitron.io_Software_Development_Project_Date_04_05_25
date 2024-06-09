from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import Album
from .forms import Album_form
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

# def album(request):
#     return render(request,'album.html',{"Title":"Album Page"})

@method_decorator(login_required,name='dispatch')
class AddAlbum(CreateView):
    model = Album
    form_class = Album_form
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')

    def form_valid(self,form):
        form.save()
        messages.success(self.request,"You have successfully add an album.")
        return super().form_valid(form)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Album Page"
        return context
    
@method_decorator(login_required,name='dispatch')
class EditAlbum(UpdateView):
    model = Album
    form_class = Album_form
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

    def form_valid(self,form):
        form.save()
        messages.success(self.request,"You have successfully updated an album")
        return super().form_valid(form)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Edit Album Page"
        return context
    
@method_decorator(login_required,name='dispatch')
class DeleteAlbum(DeleteView):
    model = Album
    template_name = 'delete_album.html'
    success_url  = reverse_lazy('homepage')
    pk_url_kwarg = 'id'
       

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Delete Album Page"
        context['Sure'] = "Are you sure to delete this album ?"
        return context