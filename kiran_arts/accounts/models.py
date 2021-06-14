from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserInfo(User):
    address=models.TextField(max_length=300)
    pin=models.IntegerField()
    contact=models.CharField(max_length=13)
    # user=models.OneToOneField(User,on_delete=models.CASCADE)



class UserForm(UserCreationForm):
    username=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email=forms.EmailField(max_length=254,widget=forms.TextInput(attrs={'class': 'form-control'}))
    address=forms.CharField(max_length=300,widget=forms.Textarea(attrs={'class': 'form-control'}))
    pin=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1=forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2=forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}))



    class Meta:
        model=UserInfo
        fields=["username","first_name","last_name","email",'address','pin',"password1","password2"]



# Create your models here.
