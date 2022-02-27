from django.db import models
from datetime import date
from datetime import datetime
# Create your models here.

class add_customer_details(models.Model):
    id= models.IntegerField(primary_key=True,blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=10)
    onboard_date = models.DateTimeField(auto_now_add=True)
    
class inventory(models.Model):
    id= models.IntegerField(primary_key=True,blank=True)
    vehical_name = models.CharField(max_length=100)
    vehical_number = models.IntegerField(max_length=100)
    inventory_add_date = models.DateTimeField(auto_now_add=True)
    
    
class booking_details(models.Model):
    id =  models.IntegerField(primary_key=True,blank=True)
    vehical_name = models.CharField(max_length=100)
    vehical_number = models.IntegerField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=10)
    booking_date =  models.DateTimeField(auto_now_add=True)
    
    