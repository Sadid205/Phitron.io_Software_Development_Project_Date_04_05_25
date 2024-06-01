from django.urls import path
from . import views

urlpatterns = [
    path('',views.AddTask,name="AddTask"),
    path('editTask/<int:id>',views.EditTask,name="editTask"),
    path('deleteTask/<int:id>',views.deleteTask,name="deleteTask")
]
