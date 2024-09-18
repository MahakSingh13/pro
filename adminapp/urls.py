from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns =[
    path('dash',views.index,name="dash"),
    path('teacher',views.teacher,name="teacher"),
    path('student',views.student,name="student"),
    path('Attendance',views.attendance,name="Attendance"),
    path('classes',views.classes,name="classes"),
    path('subjects',views.subjects,name="subjects"),
    path('logout',views.logout,name="logout"),
    path('delteacher/<id>',views.delteacher,name="delteacher"),
    path('delstudent/<id>',views.delstudent,name="delstudent"),
    path('edit/<id>',views.edit,name="edit"),
    path('editteacher/<id>',views.editteacher,name="editteacher"),
    path('viewenquiry/',views.viewenquiry,name="viewenquiry"),
    path('admincp/',views.admincp,name="admincp"),
]