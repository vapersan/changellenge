from django.urls import path
from . import views

urlpatterns = [
    path('add-service/', views.add_service, name='add-service'),
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('my-services/', views.my_services, name='my-services'),
    path('profile/', views.profile, name='profile'),
]
