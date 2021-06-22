from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField()
    photo = models.ImageField(null=True, blank=True)


