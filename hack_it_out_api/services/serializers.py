from django.db import models
from rest_framework import fields, serializers
from rest_framework.serializers import ModelSerializer, ListSerializer
from .models import Service, Appointment
from users.models import StaffSchedule
class GetServicessSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'price', 'duration')

class GetDoctorsSerializer(ModelSerializer):
    doctor_id = serializers.IntegerField(source="doctor.id", read_only=True)
    doctor_name = serializers.CharField(source="doctor.name", read_only=True)
    user_from = serializers.TimeField(format="%I %p")
    user_to = serializers.TimeField(format="%I %p")

    class Meta:
        model = StaffSchedule
        fields = ('doctor_id', 'doctor_name', 'user_from', 'user_to')

class GetServiceSpecialistsSerializer(ModelSerializer):
    specialists = GetDoctorsSerializer(many=True)
    class Meta:
        model = Service
        fields = ('id',  'specialists')
        # look_field = "specialists"

class AppointmentSerializer(ModelSerializer):
    status = serializers.CharField(required=False)
    appointment_on = serializers.DateTimeField(format="%d-%m-%y %I %p")
    class Meta:
        model = Appointment
        fields = ('patient', 'doctor', 'appointment_on', 'service', 'description', 'status',)

class GetAppointmentSerializer(ModelSerializer):
    appointment_on = serializers.DateTimeField(format="%d-%m-%Y %I %p")
    specialist = serializers.CharField(source="doctor.name", read_only=True)
    service = serializers.CharField(source="service.name", read_only=True)
    price = serializers.CharField(source="service.price", read_only=True)
    class Meta:
        model = Appointment
        fields = ('id', 'specialist', 'appointment_on', 'service', 'description', 'status','price')

