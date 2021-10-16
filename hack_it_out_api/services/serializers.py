from django.db import models
from rest_framework import fields, serializers
from rest_framework.serializers import ModelSerializer, ListSerializer
from .models import Service, Appointment
from users.serializers import GetDoctorsSerializer
class GetServicessSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'price', 'duration')

class GetServiceSpecialistsSerializer(ModelSerializer):
    specialists = GetDoctorsSerializer(read_only=True, many=True)
    class Meta:
        model = Service
        fields = ('id', 'name', 'price', 'duration', 'specialists')

class AppointmentSerializer(ModelSerializer):
    status = serializers.CharField(required=False)
    appointment_on = serializers.DateTimeField(format="%d-%m-%y %I %p")
    class Meta:
        model = Appointment
        fields = ('patient', 'doctor', 'appointment_on', 'service', 'description', 'status',)

class GetAppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'doctor', 'appointment_on', 'service', 'description', 'status',)

