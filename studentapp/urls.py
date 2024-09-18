from django.urls import path
from . import views

urlpatterns=[
    path('studentapp/',views.studentdash,name="studentdash"),
    path('studentprofile/',views.studentprofile,name="studentprofile"),
    path('studentlogout/',views.studentlogout,name="studentlogout"),
    path('studentsubject/',views.studentsubject,name="studentsubject"),
    path('studentattend/',views.studentattend,name="studentattend"),
    path('studentdash/',views.studentdash,name="studentdash"),
]