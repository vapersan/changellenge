from django.urls import path
from . import views

urlpatterns = [
    path('add-service/', views.add_service, name='add-service'),
    path('liven_test/', views.liven_test),
]
