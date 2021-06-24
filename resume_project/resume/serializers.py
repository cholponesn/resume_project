from rest_framework import serializers
from .models import *

class ResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume
        fields = '__all__'

class PersonalinfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Personalinfo
        fields = '__all__'



class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        fields = '__all__'


