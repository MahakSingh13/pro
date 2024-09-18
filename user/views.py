from django.shortcuts import render,redirect,reverse
from . models import LoginUser
import datetime
from .models import Enquiry

# Create your views here.
def index(request):
    return render(request,'index.html')

def vision(request):
    return render(request,'vision.html')

def school(request):
    return render(request,'school.html')

def login(request):
    return render(request,'login.html')

def academics(request):
    return render(request,'academics.html')

def career(request):
    return render(request,'career.html')

def founder(request):
    return render(request,'founder.html')

def chairman(request):
    return render(request,'chairman.html')

def principal(request):
    return render(request,'principal.html')

def smt(request):
    return render(request,'smt.html')

def transport(request):
    return render(request,'transport.html')

def medical(request):
    return render(request,'medical.html')

def smart_class(request):
    return render(request,'smart_class.html')

def admission(request):
    return render(request,'admission.html')

def media(request):
    return render(request,'media.html')

def events(request):
    return render(request,'events.html')

def fees(request):
    return render(request,'fees.html')

def rules(request):
    return render(request,'rules.html')

def prospectus(request):
    return render(request,'prospectus.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        pname=request.POST['pname']
        area=request.POST['area']
        d=datetime.datetime.today()
        enquiry_date=d.strftime("%d-%m-%y: %M %p")
        enq=Enquiry(name=name,mobile=mobile,email=email,pname=pname,area=area,enquiry_date=enquiry_date)
        enq.save()
        return render(request,'contact.html',{'msg':"Your Enquiry is Submitted"})
    return render(request,'contact.html')

def logcode(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        usertype=request.POST['utype']
        try:
            user=LoginUser.objects.get(username=username,password=password,usertype=usertype)
            if user.usertype=="admin":
                request.session['username']=username
                return redirect('adminapp:dash')
            elif user.usertype=="student":
                request.session['student']=username
                return redirect('studentapp:studentdash')
            elif user.usertype=="teacher":
                request.session['teacher']=username
                return redirect('teacherapp:teacherdash')
        except:
            return redirect('login')
        
