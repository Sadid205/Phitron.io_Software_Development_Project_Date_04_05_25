from django.urls import path
from . import views
urlpatterns = [
    path('',views.Album,name="albumPage"),
    path('edit/<int:id>',views.Edit,name="EditAlbum"),
    path('delete/<int:id>',views.DeleteAlbum,name="DeleteAlbum")
]
