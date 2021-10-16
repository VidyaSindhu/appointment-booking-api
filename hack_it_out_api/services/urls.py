from django.urls import path
from django.urls.conf import include
from .views import BookAppointmentView, GetServiceView
# from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('service/', GetServiceView.as_view()), #GET
    path('appointment/book/', BookAppointmentView.as_view()), #POST
    
]