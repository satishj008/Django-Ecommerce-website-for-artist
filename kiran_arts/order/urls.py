
from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('check',v.checkout_view,name="checkout"),
    path('view',v.order_view,name="orderview"),
]
