from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *

class ProfileSerializer(serializers.ModelSerializer):

     class Meta:
         model = Profile
         fields = ['full_name' ]

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','password']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=5)
    password = serializers.CharField()


