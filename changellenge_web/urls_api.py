from django.urls import path
from . import api

urlpatterns = [
    path('get-services/', api.get_services, name='api-get-services'),
    path('get-service/<int:id_>/', api.get_service, name='api-get-service'),
    path('get-service-count/', api.get_service_count, name='api-get-service-count'),
]
