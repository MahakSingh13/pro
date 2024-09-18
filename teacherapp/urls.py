from django.urls import path
from . import views

urlpatterns=[
    path('teacherapp/',views.teacherdash,name="teacherdash"),
    path('teacherlogout/',views.teacherlogout,name="teacherlogout"),
    path('teachersubject/',views.teachersubject,name="teachersubject"),
    path('teacherattend/',views.teacherattend,name="teacherattend"),
    path('teacherprofile/',views.teacherprofile,name="teacherprofile"),
    path('teacherdash/',views.teacherdash,name="teacherdash"),
]