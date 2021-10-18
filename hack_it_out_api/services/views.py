from rest_framework.response import Response

from .serializers import AppointmentSerializer, GetAppointmentSerializer, GetServicessSerializer, GetServiceSpecialistsSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from .models import Service, Appointment
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from users.models import StaffSchedule, User
# Create your views here.

class GetServiceView(ListAPIView):
    queryset = Service.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JSONWebTokenAuthentication,]
    serializer_class = GetServicessSerializer
    APIView = ['GET']

class GetServiceSpeicialistsView(RetrieveAPIView):
    queryset = Service.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication,]
    serializer_class = GetServiceSpecialistsSerializer
    APIView = ['GET']
    
class GetAppointmentDetailView(RetrieveAPIView):
    queryset = Appointment.objects.all()
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
        patient = User.objects.get(pk=request.user.id)
        self.queryset = patient.patient_appointments.all()
        return super().get(request, *args, **kwargs)

        
class BookAppointmentView(CreateAPIView):
    queryset = Appointment.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication,]
    serializer_class = AppointmentSerializer
    APIView = ['POST']

    def create(self, request, *args, **kwargs):
        request.data["patient"] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"success":True}, status=201, headers=headers)


class ModifyAppointmentView(UpdateAPIView):
    APIView = ['PATCH']
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer(partial=True)
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication,]

    def update(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        appointment = Appointment.objects.get(pk=pk)
        appointment.status = request.data["status"]
        appointment.save()

        return Response({"success":True}, status=200)

