from rest_framework import serializers
from .models import *

class ResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume
        fields = '__all__'

class PersonalinfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Personalinfo
        exclude = ['resume']



class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        exclude = ['resume']

class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        exclude = ['resume']


