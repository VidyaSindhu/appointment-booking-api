from django.db import models
from rest_framework import fields, serializers
from rest_framework.serializers import ModelSerializer
from .models import Service, Appointment

class GetServicessSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'price', 'duration')

class BookAppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('user_id', 'doctor', 'appointment_on', 'service_id', 'description')

