from django.db import models
from rest_framework import fields, serializers
from rest_framework.serializers import ModelSerializer
from .models import Service, Appointment

class GetServicessSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'price', 'duration')

class AppointmentSerializer(ModelSerializer):
    status = serializers.CharField(required=False)
    class Meta:
        model = Appointment
        fields = ('doctor', 'appointment_on', 'service_id', 'description', 'status',)

class GetAppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'doctor', 'appointment_on', 'service_id', 'description', 'status',)

