
from django.contrib import admin
from django.urls import path
from .import views as v
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('fbycat/<int:id>',v.filter_by_cat,name="filter_by_cat"),
    path('fbycat',v.filter_by_cat,name="filter_by_cat"),
    path('gig/<int:id>',v.gig_view,name="gig"),
    path('search',v.search,name="search"),
    path('serreg',v.service_reg,name="serreg"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
