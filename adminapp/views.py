from django.shortcuts import render,redirect,reverse
import datetime
from user.models import *

# Create your views here.
def index(request):
    if request.session['username']!=None:
        stu_count=Student.objects.all().count()
        t_count=Teacher.objects.all().count()
        cl_count=Class.objects.all().count()
        sub_count=Class.objects.all().count()
        return render(request,'adminhome.html',locals())   
    else:
        return reverse(redirect('login'))   
    
def teacher(request):
    # try:
        if request.session['username']!=None:
            if request.method=="POST":
                name=request.POST['name']
                number=request.POST['number']
                email=request.POST['email']
                qua=request.POST['qualification']
                exp=request.POST['exp']
                tsalary=request.POST['tsalary']
                tclass=request.POST['tclass']
                address=request.POST['address']
                password=request.POST['password']
                created=datetime.datetime.today()
                teacher=Teacher (
                    name=name,
                    number=number,
                    email=email,
                    qualification=qua,
                    experience=exp,
                    tsalary=tsalary,
                    tclass=tclass, 
                    address=address,
                    created=created,
                    )
                teacher.save()
                log=LoginUser(username=email,password=password,usertype="teacher")
                log.save()
                t=Teacher.objects.all()
                cl=Class.objects.all()
                return render(request,'teacher.html',{'msg':"Teacher is Added",'t':t,'cl':cl})
            t=Teacher.objects.all()
            cl=Class.objects.all()
            return render(request,'teacher.html',{'t':t,'cl':cl})
    # except:
        # return redirect('login') 
    
def student(request):
    try:
        if request.session['username']!=None:
            if request.method=="POST":
                name=request.POST['name']
                fname=request.POST['fname']
                email=request.POST['email']
                mobile=request.POST['number']
                fnumber=request.POST['fnumber']
                dob=request.POST['dob']
                sclass=request.POST['sclass']
                sfee=request.POST['sfee']
                balance=request.POST['balance']
                address=request.POST['address']
                password=request.POST['password']
                stu=Student(
                    name=name,
                    fname=fname,
                    mobile=mobile,
                    email=email,
                    fnumber=fnumber,
                    dob=dob,
                    sclass=sclass,
                    sfee=sfee,
                    balance=balance,
                    address=address,
                )
                stu.save()
                log=LoginUser(username=email,password=password,usertype="student")
                log.save()
                msg="Student is added successfully"
                stu=Student.objects.all()
                cl=Class.objects.all()
                
                return render(request,'student.html',{'msg':msg,'stu':stu, 'cl':cl,})
            stu=Student.objects.all()
            cl=Class.objects.all()
            sub=Class.objects.all()
            return render(request,'student.html',{'stu':stu,'cl':cl})
    except:
        return redirect('login')


def attendance(request):
    try:
        if request.session['username']!=None:
            attend=StudentAttendance.objects.all()
            return render(request,'attendance.html',{'attend':attend})
    except:
        return render(request,'login')


    
def logout(request):
    try:
        if request.session['username']!=None:
            del request.session['username']
            return redirect('login')
    except:
        return redirect('login')
    
def delteacher(request,id):
    try:
        if request.session['username']!=None:
            Teacher.objects.get(id=id).delete()
            return redirect('adminapp:teacher')
    except:
        return redirect('login')
    
def delstudent(request,id):
    try:
        if request.session['username']!=None:
            Student.objects.get(id=id).delete()
            return redirect('adminapp:student')
    except:
        return redirect('login')
    
def edit(request,id):
    try:
        if request.session['username']!=None:
            stu=Student.objects.get(id=id)
            cl=Class.objects.all()
            if request.method=="POST":
                name=request.POST['name']
                fname=request.POST['fname']
                mobile=request.POST['number']
                email=request.POST['email']
                fnumber=request.POST['fnumber']
                dob=request.POST['dob']
                sclass=request.POST['sclass']
                sfee=request.POST['sfee']
                balance=request.POST['balance']
                address=request.POST['address']
                Student.objects.filter(id=id).update(
                    name=name,
                    fname=fname,
                    mobile=mobile,
                    email=email,
                    fnumber=fnumber,
                    dob=dob,
                    sclass=sclass,
                    sfee=sfee,
                    balance=balance,
                    address=address,
                    )
                return redirect('adminapp:student')
            return render(request,'edit.html',{'stu':stu,'cl':cl})
    except:
        return redirect('login')
        
def editteacher(request,id):
    try:
        if request.session['username']!=None:
            t=Teacher.objects.get(id=id)
            if request.method=="POST":
                name=request.POST['name']
                address=request.POST['address']
                email=request.POST['email']
                experience=request.POST['exp']
                number=request.POST['number']
                qualification=request.POST['qualification']
                tclass=request.POST['tclass']
                tsalary=request.POST['tsalary']
                # created=request.POST['created']
                
                Teacher.objects.filter(id=id).update(
                    name=name,
                    address=address,
                    email=email,
                    
                    experience=experience,
                    number=number,
                    qualification=qualification,
                    tclass=tclass,
                    tsalary=tsalary,
                    # created=created,
                    )
                return redirect('adminapp:teacher')
            return render(request,'editteacher.html',{'t':t})
    except:
        return redirect('login')
        
def classes(request):
    try:
        if request.session['username']!=None:
            c=Class.objects.all()
            if request.method=="POST":
                name=request.POST['name']
                roomno=request.POST['roomno']
                seats=request.POST['seats']
                c=Class(name=name,roomno=roomno,seats=seats)
                c.save()
                return redirect('adminapp:classes')
            return render(request,'classes.html',locals())
    except:
         return render(request,'login')
    
def subjects(request):
    try:
        if request.session['username']!=None:
            cl=Class.objects.all()
            sub=Subject.objects.all()
            teacher=Teacher.objects.all()
            if request.method=="POST":
                name=request.POST['name']
                classid=request.POST['classid']
                teacherid=request.POST['teacherid']
                book=request.POST['book']
                s=Subject(name=name,classid=classid,teacherid=teacherid,book=book)
                s.save()
                return redirect('adminapp:subjects')
            return render(request,'subjects.html',locals())
    except:
        return render(request,'login')
    
def viewenquiry(request):
    try:
        if request.session['username']!=None:
            enq=Enquiry.objects.all()
            return render(request,'viewenquiry.html',locals())   
    except:
        return redirect('login')

def admincp(request):
    # try:
        if request.session['username']!=None:
            adminid=request.session['username']
            if request.method=="POST":
                oldpassword=request.POST['oldpassword']
                newpassword=request.POST['newpassword']
                cpassword=request.POST['cpassword']
                try:
                    obj=LoginUser.objects.get(username=adminid,password=oldpassword)
                    if newpassword!=cpassword:
                        msg="Enter same Password"
                    elif oldpassword==obj.password:
                        LoginUser.objects.filter(username=adminid,password=oldpassword).update(password=newpassword)
                        return redirect('adminapp:logout')
                except:
                    return render(request,'admincp.html',{'msg':"Invali Old Password"})
            return render(request,'admincp.html',locals())   
    # except:
        # return redirect('login')
        
