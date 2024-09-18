from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('vission-mission',views.vision,name="vision"),
    path('about-school',views.school,name="about-school"),
    path('login',views.login,name="login"),
    path('logcode',views.logcode,name="logcode"),
    path('academics',views.academics,name="academics"),
    path('career',views.career,name='career'),
    path('founder',views.founder,name='founder'),
    path('chairman',views.chairman,name='chairman'),
    path('principal',views.principal,name='principal'),
    path('smt',views.smt,name='smt'),
    path('transport',views.transport,name='transport'),
    path('medical',views.medical,name='medical'),
    path('smart_class',views.smart_class,name='smart_class'),
    path('admission',views.admission,name='admission'),
    path('contact',views.contact,name='contact'),
    path('media',views.media,name='media'),
    path('events',views.events,name='events'),
    path('fees',views.fees,name='fees'),
    path('rules',views.rules,name='rules'),
    path('prospectus',views.prospectus,name='prospectus'),

]
