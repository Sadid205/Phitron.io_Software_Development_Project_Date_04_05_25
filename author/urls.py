from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
]
