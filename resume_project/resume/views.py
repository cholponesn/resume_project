from django.http import request
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from .models import *

class ResumeView(APIView):

    def get(self,request):
        resume = Resume.objects.all()
        serializer = ResumeSerializer(resume,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)






class PersonalinfoView(APIView):

    def post(self,request):
        serializer = PersonalinfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

class EducationView(APIView):
    def post(self,request):
        serializer = EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

class ExperienceView(APIView):
    def post(self,request):
        serializer = ExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
















