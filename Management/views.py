from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from Management.models import *

# Create your views here.




def dummy(request):
    if not request.user.is_staff:
        return redirect('Login')
    return render(request,'dummy.html')

def index(request):
    if not request.user.is_staff:
        return redirect('Login')
    doctors=Doctor.objects.all()
    patients=Patient.objects.all()
    appointments=Appointment.objects.all()

    d=0
    p=0
    a=0
    for i in doctors:
        d+=1
    for i in patients:
        p+=1
    for i in appointments:
        a+=1
    d1={'d':d,'p':p,'a':a}
    return render(request,'index.html',d1)

def Login(request):
    error=''
    if request.method=='POST':
        u=request.POST['an']
        p=request.POST['pw']
        user=authenticate(username=u,password=p)

        try:
            if  user.is_staff:
                login(request,user)
                error='no'
            else:
                error='yes'

        except:
             error='yes'
    d={'error':error}
    return render(request,'Login.html',d)

def Logout(request):
    if not request.user.is_staff:
        return redirect('Login')
    logout(request)
    return redirect('Login')


def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def view_doctor(request):
    if not request.user.is_staff:
        return redirect('Login')
    doc=Doctor.objects.all()
    d={"doc":doc}
    return render(request,'view_doctor.html',d)

def add_doctor(request):
    error=''
    if request.method=='POST':
        n=request.POST['an']
        c=request.POST['co']
        g=request.POST['g']
        s=request.POST['sc']

        try:
            doc=Doctor.objects.create(name=n,mobile=c,gender=g,specialization=s)
            error='no'
        except:
            error='yes'
    d={'error':error}
    return render(request,'add_doctor.html',d)

def delete_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('Login')
    
    doc=Doctor.objects.get(id=pid)
    doc.delete()
    return redirect('view_doctor')

def view_patient(request):
    if not request.user.is_staff:
        return redirect('Login')
    pat=Patient.objects.all()
    d={"pat":pat}
    return render(request,'view_patient.html',d)

def add_patient(request):
    error=''
    if request.method=='POST':
        n=request.POST['an']
        c=request.POST['co']
        g=request.POST['g']
        s=request.POST['ad']

        try:
            doc=Patient.objects.create(pname=n,gender=g,pmobile=c,address=s)
            error='no'
        except:
            error='yes'
    d={'error':error}
    return render(request,'add_patient.html',d)

def delete_patient(request,pid):
    if not request.user.is_staff:
        return redirect('Login')

    pat=Patient.objects.get(id=pid)
    pat.delete()
    return redirect('view_patient')


def view_appointment(request):
    if not request.user.is_staff:
        return redirect('Login')
    appo=Appointment.objects.all()
    d={"appo":appo}
    return render(request,'view_appointment.html',d)


def add_appointment(request):
    error=''
    do=Doctor.objects.all()
    pa=Patient.objects.all()
    if request.method=='POST':
        d=request.POST['doctor']
        p=request.POST['patient']
        d1=request.POST['date']
        t=request.POST['time']

        doc1=Doctor.objects.filter(name=d).first()
        pa1=Patient.objects.filter(pname=p).first()
        try:
            doc=Appointment.objects.create(doctor=doc1,patient=pa1,date=d1,time=t)
            error='no'
        except:
            error='yes'
    d={'error':error,'do':do,'pa':pa}
    return render(request,'add_appointment.html',d)

def delete_appointment(request,pid):
    if not request.user.is_staff:
        return redirect('Login')

    appo=Appointment.objects.get(id=pid)
    appo.delete()
    return redirect('view_appointment')