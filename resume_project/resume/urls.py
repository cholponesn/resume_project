from django.urls import path
from .views import *

urlpatterns = [
   path('resume/',ResumeView.as_view()),
   path('personalinfo/',PersonalinfoView.as_view()),
   path('education/',EducationView.as_view()),
   path('experience/',ExperienceView.as_view()),


]
