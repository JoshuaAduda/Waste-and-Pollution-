from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
   path('home/', views.home, name='home'),
   path('maps/', views.maps, name='maps'),
   path('report/', views.report, name='report'),
   path('eventsAndActivities/', views.eventsAndActivities, name='eventsAndActivities')
 ]
