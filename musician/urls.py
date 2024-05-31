from django.urls import path
from . import views
urlpatterns = [
    path('',views.musician,name="musicianPage"),
    path('edit/<int:id>',views.EditMusician,name="EditMusician")
]
