from django.urls import path
from django.urls.conf import include
from .views import BookAppointmentView, GetAppointmentDetailView, GetAppointmentsView, GetServiceSpeicialistsView, GetServiceView, ModifyAppointmentView
# from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', GetServiceView.as_view()), #GET
    path('<int:pk>/', GetServiceSpeicialistsView.as_view()), #GET
    path('appointment/book/', BookAppointmentView.as_view()), #POST
    path('appointment/update/<int:pk>/', ModifyAppointmentView.as_view()), #PATCH, DELETE
    path('appointment/all', GetAppointmentsView.as_view()), #GET
    path('appointment/<int:pk>/', GetAppointmentDetailView.as_view()), #GET
]