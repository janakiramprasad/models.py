from django.shortcuts import render

from app.models import *

# Create your views here.

def diplay(request):
    QLCO=Country.objects.all()
    d={'country':QLCO}
    return render(request,'diplay.html',d)

def display1(request):
    QLCA=Capital.objects.all()
    p={'capital':QLCA}
    return render(request,'display1.html', p)

def display2(request):
    QLDT=Dept.objects.all()
    r={'dept':QLDT}
    return render(request,'display2.html',r)

def display3(request):
    QLEM=Emp.objects.all()
    m={'employee':QLEM}
    return render(request,'display3.html',m)