from django.shortcuts import render

from app.models import *

from django.http import HttpResponse

from django.db.models.functions import Length

# Create your views here.

def diplay(request):
    QLCO=Country.objects.all()
    QLCO=Country.objects.all().order_by('country_ID')
    QLCO=Country.objects.all().order_by('-country_ID')
    QLCO=Country.objects.all().order_by('country_ID')
    QLCO=Country.objects.all().order_by(Length('country_name'))
    QLCO=Country.objects.all().order_by(Length('country_name').desc())
    QLCO=Country.objects.all()[2:6]
    QLCO=Country.objects.all().exclude(country_name='india')
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

def insert_country(request):
    countryid=input('country country id')
    countryName=input('enter country name')
    cno=Country.objects.get_or_create(country_ID=countryid,country_name=countryName)[0]
    cno.save()
    return HttpResponse('DATA INSERTED')



