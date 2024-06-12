from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('signup/',views.UserSignUp,name="signup"),
    path('login/',views.UserLogin.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('profile/',views.Profile,name="profile"),
    path('profile/edit/',views.EditProfile,name="edit_profile"),
    path('profile/change_pass/',views.ChangePassword,name="change_password"),
    path('buy/<int:id>/',views.Buy,name="buy")
]
