from django.contrib import admin
from django.urls import path
from Register import views

urlpatterns = [
    path('', views.index, name='Register'),
    path('about', views.about, name='Register'),
    path('services', views.services, name='Register'),
    path('contact', views.contact, name='Register'),
    
]
