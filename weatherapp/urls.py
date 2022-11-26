from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path 
from weatherapp import views


urlpatterns = [
    path('',views.index,name='home'),
    path('weather',views.weather , name='weather'),
    path('about',views.about,name='about'),
    # path('404',views.error,name='error')
    
]
