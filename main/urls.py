from turtle import home
from django.urls import path
from .views import home, clicker #check_values

urlpatterns = [
    path('', home, name='home'),
    path('clicker', clicker, name='clicker'),
    #path('check_values', check_values, name='check_values')
]
