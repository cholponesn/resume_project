from django.contrib.auth.models import User
from django.db import models


class Resume(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)




class Personalinfo(models.Model):
    full_name = models.CharField(max_length=20)
    email = models.EmailField()
    date_birth = models.DateField()
    phone = models.IntegerField()
    address = models.CharField(max_length=10)
    photo = models.ImageField(null=True, blank=True)
    bio = models.CharField(max_length=500)
    resume = models.ForeignKey(Resume,on_delete=models.SET_NULL,null=True)

class Education(models.Model):
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True)
    school_name = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100)
    resume = models.ForeignKey(Resume,on_delete=models.SET_NULL,null=True)


class Experience(models.Model):
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True)
    company = models.CharField(max_length=15)
    responsibilities = models.CharField(max_length=500)
    resume = models.ForeignKey(Resume,on_delete=models.SET_NULL,null=True)








