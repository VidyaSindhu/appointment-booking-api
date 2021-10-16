from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import BookAppointmentSerializer, GetServicessSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Service, Appointment
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# Create your views here.

class GetServiceView(ListAPIView):
    queryset = Service.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JSONWebTokenAuthentication,]
    serializer_class = GetServicessSerializer
    APIView = ['GET']

class BookAppointmentView(CreateAPIView):
    queryset = Service.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication,]
    serializer_class = BookAppointmentSerializer
    APIView = ['POST']