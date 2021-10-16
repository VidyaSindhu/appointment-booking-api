from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

class UserDetailSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'name', 'address')
    
class UserRegisterSerializer(ModelSerializer):
       
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'name', 'address', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            name=validated_data['name'],
            address=validated_data['address']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('password', 'old_password')

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(False)
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance 


