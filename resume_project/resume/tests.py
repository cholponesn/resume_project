from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import *




class PersonalinfoTest(APITestCase):

     def setUp(self):
         resume = Resume.objects.create()

         self.url = reverse('personalinfo',args=(resume.id,))

     def test_personalinfo_ok(self):
         data = {
             "full_name": "cholpon",
             "email":"cholpon@gmail.com",
             "date_birth":"2020-07-05",
             "address":"babaeva 60",
             "bio":"hghghgh"
         }
         self.response = self.client.post(self.url, data, format="json")
         self.assertEqual(self.response.status_code, 201)


class EducationTest(APITestCase):

    def setUp(self):
        resume = Resume.objects.create()

        self.url = reverse('education',args=(resume.id,))

    def test_education_ok(self):
        data = {"start_year": 2015,
                "end_year": 2018,
                "school_name": "Academy of tourism",
                "specialization": "Manager"


        }

        self.response = self.client.post(self.url, data, format="json")
        self.assertEqual(self.response.status_code, 201)

class ExperienceTest(APITestCase):

    def setUp(self):
        resume = Resume.objects.create()
        self.url = reverse('experience',args=(resume.id,))

    def test_experience_ok(self):
        data = {"start_year": 2020,
                "end_year": 2021,
                "company": "Google",
                "responsibilities": "backend разработчик"

        }

        self.response = self.client.post(self.url, data, format="json")
        self.assertEqual(self.response.status_code, 201)




