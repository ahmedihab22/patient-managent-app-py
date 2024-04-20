from django.contrib import admin
from django.urls import path ,include
from . import views
urlpatterns = [
   path('',views.home,name="home"),
   path('register',views.register,name='register'),
   path('search',views.search,name='search'),
   path('',views.patients,name="patients"),
   path('index',views.index,name='index'),
]
