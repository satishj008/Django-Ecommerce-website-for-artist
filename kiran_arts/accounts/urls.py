
from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path("register",v.add_user,name="register"),
    path("login",v.login_view,name="login"),
    path("login/<int:sid>",v.login_view,name="login"),
    path("logout",v.logout_view,name="logout"),
    path("contact",v.contact_view,name="contact"),


]
