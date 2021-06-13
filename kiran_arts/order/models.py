from django.db import models
from django.contrib.auth.models import User
from products.models import Service,PlanPrice
from django import forms
from django.contrib.postgres.fields import ArrayField

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    orderdate=models.DateField(auto_now=True)
    service_price=models.CharField(max_length=300)

    # service_price=ArrayField(ArrayField(models.IntegerField()))
    orderstatus=models.CharField(max_length=30,default="Processing")
    totalbill=models.IntegerField()
    ship_first_name=models.CharField(max_length=30)
    ship_last_name=models.CharField(max_length=30)
    ship_email=models.EmailField(max_length=254)
    ship_contact=models.CharField(max_length=13)
    ship_country=models.CharField(max_length=30)
    ship_state=models.CharField(max_length=30)
    ship_address=models.TextField(max_length=300)
    ship_pin=models.IntegerField()
    payment=models.CharField(max_length=30)



# Create your models here.
