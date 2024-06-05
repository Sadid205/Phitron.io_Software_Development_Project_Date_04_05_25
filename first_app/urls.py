from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('register/',views.register_user,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/change_pass1',views.withPass,name='change_pass_with'),
    path('profile/change_pass2',views.withoutPass,name='change_pass_without')
]
