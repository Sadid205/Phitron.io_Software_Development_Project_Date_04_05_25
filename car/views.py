from django.shortcuts import render
from .forms import CarForm,CommentForm
from .models import Car
from django.views.generic import CreateView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required,name='dispatch')
class CarFormPost(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'AddCar.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        
        context['title'] = "Add Post Form"
        context['buttonName'] = "Post"

        return context

class CarDetails(DetailView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = 'CarDetails.html'

    def post(self,request,*args,**kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(self,request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = CommentForm()
        context['title'] = 'Car Details Page'
        context['comments'] = comments
        context['comment_form'] = comment_form

        return context
