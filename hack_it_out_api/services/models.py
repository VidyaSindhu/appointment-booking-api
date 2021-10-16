from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DurationField
from users.models import User
# Create your models here.

class Service(models.Model):
    name = models.CharField(default="",max_length=255)
    price = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    doctor = models.ForeignKey(User, on_delete=CASCADE, related_name="doctor")
    appointment_on = models.DateTimeField()
    status = models.CharField(default="pending", max_length=255)
    service = models.ForeignKey(Service, on_delete=CASCADE)
    description = models.CharField(default=None, max_length=255)
