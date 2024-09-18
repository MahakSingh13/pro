from django.db import models

# Create your models here.
class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    fname=models.CharField(max_length=25)
    mobile=models.CharField(max_length=12)
    email=models.CharField(max_length=30)
    fnumber=models.CharField(max_length=11)
    dob=models.CharField(max_length=20)
    sclass=models.CharField(max_length=10)
    sfee=models.CharField(max_length=20)
    balance=models.IntegerField()
    pic=models.FileField()
    address=models.TextField()

class Teacher(models.Model):
    id=models.AutoField(primary_key=True)
    address=models.TextField()
    email=models.CharField(max_length=30)
    experience=models.CharField(max_length=30)
    name=models.CharField(max_length=25)
    number=models.CharField(max_length=25)
    pic=models.FileField(upload_to='')
    qualification=models.CharField(max_length=30)
    tclass=models.CharField(max_length=30)
   
    tsalary=models.CharField(max_length=12)
    created=models.CharField(max_length=25)
        
class LoginUser(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=8)
    usertype=models.CharField(max_length=30)

class StudentAttendance(models.Model):
    id=models.AutoField(primary_key=True)
    studentid=models.CharField(max_length=10)
    studentname=models.CharField(max_length=30,default="")
    sclass=models.CharField(max_length=20,default="")
    date=models.DateField()
    status=models.CharField(max_length=15)

class Subject(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    classid=models.CharField(max_length=24)
    teacherid=models.CharField(max_length=25)
    book=models.FileField()
                        
class Class(models.Model):
    id=models. AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    roomno=models.CharField(max_length=5)
    seats=models.IntegerField()

class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=15)
    email=models.CharField(max_length=50)
    pname=models.CharField(max_length=50)
    area=models.TextField()
    enquiry_date=models.CharField(max_length=25)
    
   



