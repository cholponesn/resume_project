from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email','photo']

admin.site.register(Profile,ProfileAdmin)



