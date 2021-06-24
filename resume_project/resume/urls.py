from django.urls import path
from .views import *

urlpatterns = [
   path('resume/',ResumeView.as_view()),
   path('personalinfo/<int:resume_id>/',PersonalinfoView.as_view(),name='personalinfo'),
   path('education/<int:resume_id>/',EducationView.as_view(),name='education'),
   path('experience/<int:resume_id>/',ExperienceView.as_view(),name='experience'),


]
