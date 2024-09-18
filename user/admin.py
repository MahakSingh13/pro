from django.contrib import admin
from .models import Student
from .models import Teacher
from .models import LoginUser
from .models import StudentAttendance
from .models import Subject
from .models import Class

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(LoginUser)
admin.site.register(StudentAttendance)
admin.site.register(Subject)
admin.site.register(Class)