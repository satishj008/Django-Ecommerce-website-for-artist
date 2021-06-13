from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [

    path("view",v.cart,name="cart_view"),
    path("view/<int:id>",v.cart,name="cart_view"),
    path("add/<int:sid>/<int:ppid>",v.add_cart,name="addcart"),
    # path("delete/<int:id>",v.delete_cart,name="delete"),
]
