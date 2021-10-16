from functools import partial, partialmethod
from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .serializers import AppointmentSerializer, GetAppointmentSerializer, GetServicessSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from .models import Service, Appointment
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from users.models import User
# Create your views here.

class GetServiceView(ListAPIView):
    queryset = Service.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JSONWebTokenAuthentication,]
    serializer_class = GetServicessSerializer
    APIView = ['GET']

class GetAppointmentDetailView(RetrieveAPIView):
    queryset = Appointment.patient_appointments.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication,]
    serializer_class = GetAppointmentSerializer
    APIView = ['GET']

class GetAppointmentsView(ListAPIView):
    queryset = Appointment.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication,]
    serializer_class = GetAppointmentSerializer
    APIView = ['GET']

    def get(self, request, *args, **kwargs):
        patient = User.objects.get(pk=self.kwargs['pk'])
        self.queryset = patient.patient_appointments.all()
        return super().get(request, *args, **kwargs)

        
class BookAppointmentView(CreateAPIView):
    queryset = Appointment.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication,]
    serializer_class = AppointmentSerializer
    APIView = ['POST']

class ModifyAppointmentView(UpdateAPIView):
    APIView = ['PATCH']
    queryset = Appointment.objects.al()
    serializer_class = AppointmentSerializer(partial=True)
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication,]

