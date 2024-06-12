from django.urls import path
from . import views

urlpatterns = [
    path('add_car/',views.CarFormPost.as_view(),name="add_car"),
    path('details/<int:id>/',views.CarDetails.as_view(),name='car_details')
]
