from typing import Any
from django.db import models

# Create your models here.
class Country(models.Model):
    country_ID=models.IntegerField(primary_key=True)
    country_name=models.CharField(max_length=100)

    def __str__(self):
        return self.country_name
    
class Capital(models.Model):
    country_ID=models.OneToOneField(Country, on_delete=models.CASCADE)
    capital=models.CharField(max_length=100)
    country_code=models.IntegerField(default=True)

    def __str__ (self):
        return self.capital



class Dept(models.Model):
    Dept_no=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)

    def __str__(self):
        return self.dname
    
class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    Dept_no=models.OneToOneField(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename
    


        
