from datetime import date
from django.contrib.auth import login
from rest_framework.decorators import api_view, permission_classes
from .models import CustomUser
from rest_framework.authtoken.views import ObtainAuthToken

from django.contrib.auth.models import update_last_login
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework import exceptions
from .serializers import ChangePasswordSerializer, UserDetailSerializer, UserRegisterSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from random import randint
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from rest_framework_jwt.views import verify_jwt_token


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class JSONWebTokenAuthentication(JSONWebTokenAuthentication):
    JSONWebTokenAuthentication.keyword = "Bearer"


def send_otp(email):
    receiver_address = email
    sender_address = 'momspizzakitchen@gmail.com'
    sender_pass = 'momspizza.1234'
    otp = randint(100000, 1000000)
    mail_content = "Hey there, /n Your One Time Password for verification is: " + \
        str(otp) + "."

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    # The subject line
    message['Subject'] = 'OTP for Registration from Moms Pizza'
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    # login with mail_id and password
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    return Response(data={"otp": otp}, status=200)




class RegisterUser(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny,]
    def create(self, request, *args, **kwargs):
        try:
            # send_otp(request.data['email'])
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            
        except Exception as e:
            print(e)
            if str(e) == "{'email': [ErrorDetail(string='custom user with this email address already exists.', code='unique')]}":
                return Response(data={"success": False, "exists": True}, status=409)
            if type(e) == exceptions.ParseError or type(e) == exceptions.ValidationError:
                return Response(data={"success": False}, status=406)
            return Response(data={"success": False}, status=500)

        else:
            user_data = CustomUser.objects.get(email=request.data["email"])
            print(user_data)
            payload = JWT_PAYLOAD_HANDLER(user_data)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user_data)

            return Response(data={"token": jwt_token, "success": True, "exists": False}, status=201)



class GetUsersDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication, BasicAuthentication]
    APIView = ['GET','PUT']
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}
        except Exception as e:
            print(e)
            return Response(data={"success": False}, status=400)
        else:
            return Response(data={"success": True}, status=202)

class GetUsersList(ListAPIView):
    APIView = ['GET']
    permission_classes = [IsAdminUser]
    authentication_classes = [BasicAuthentication]
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer

@permission_classes([AllowAny])
def check_user_existence(request):
    try:
        CustomUser.objects.get(email=request.headers.get("email"))
    except CustomUser.DoesNotExist:
        return Response(data={"exists": False}, status=200)
    else:
        return Response(data={"exists": True}, status=200)

class ChangePasswordView(UpdateAPIView):

    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication, JSONWebTokenAuthentication]
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        try:
            super().update(request, *args, **kwargs)
        except Exception as e:
            return Response(data={"success": False, "password_changed": False}, status=403)
        return Response(data={"success": True, "password_changed": True}, status=201)

