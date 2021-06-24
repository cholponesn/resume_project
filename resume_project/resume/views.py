from django.http import request
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from .models import *

class ResumeView(APIView):

    def get(self,request):
        resume = Resume.objects.filter(user=request.user)
        serializer = ResumeSerializer(resume,many=True)
        return Response(serializer.data)

    def post(self,request):
        new_resume = Resume.objects.create(user=request.user)
        serializer = ResumeSerializer(new_resume)
        return Response(serializer.data, status=201)



class PersonalinfoView(APIView):

    def post(self,request,**kwargs):
        resume = Resume.objects.get(id=kwargs['resume_id'])
        serializer = PersonalinfoSerializer(data=request.data)
        if serializer.is_valid():
            Personalinfo.objects.create(full_name=serializer.data.get('full_name'),
                                        email=serializer.data.get('email'),
                                        date_birth=serializer.data.get('date_birth'),
                                        phone=serializer.data.get('phone'),
                                        address=serializer.data.get('address'),
                                        photo=serializer.data.get('photo'),
                                        bio=serializer.data.get('bio'),
                                        resume=resume)


            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

class EducationView(APIView):
    def post(self,request,**kwargs):
        resume = Resume.objects.get(id=kwargs['resume_id'])

        serializer = EducationSerializer(data=request.data)
        if serializer.is_valid():
            Education.objects.create(start_year=serializer.data.get('start_year'),
                                     end_year=serializer.data.get('end_year'),
                                     school_name=serializer.data.get('school_name'),
                                     specialization=serializer.data.get('specialization'),
                                     resume=resume)

            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

class ExperienceView(APIView):
    def post(self,request,**kwargs):
        resume = Resume.objects.get(id=kwargs['resume_id'])

        serializer = ExperienceSerializer(data=request.data)
        if serializer.is_valid():
            Experience.objects.create(start_year=serializer.data.get('start_year'),
                                      end_year=serializer.data.get('end_year'),
                                      company=serializer.data.get('company'),
                                      responsibilities=serializer.data.get('responsibilities'),
                                      resume=resume)

            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
















