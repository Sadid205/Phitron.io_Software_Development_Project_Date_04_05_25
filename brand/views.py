from django.shortcuts import render
from .forms import BrandForm
from .models import Brand
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

@method_decorator(login_required,name='dispatch')
class AddBrand(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'AddBrand.html'
    success_url = reverse_lazy('add_brand')

    # def form_valid(self,form):
    #    return super().form_valid(form)
    
    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Add Brand Page'
    #     context['buttonName'] = 'Add'
    #     return context


