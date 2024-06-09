from django.urls import path
from . import views
urlpatterns = [
    path('add/',views.AddAlbum.as_view(),name='add_album'),
    path('edit/<int:id>',views.EditAlbum.as_view(),name='edit_album'),
    path('delete/<int:id>',views.DeleteAlbum.as_view(),name='delete_album')
]
