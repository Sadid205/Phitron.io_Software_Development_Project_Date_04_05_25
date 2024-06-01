from django.urls import path
from . import views

urlpatterns = [
    path('',views.AddCategory,name="AddCategory")
]
