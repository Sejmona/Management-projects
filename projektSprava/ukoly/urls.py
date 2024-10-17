from django.urls import path
from . import views

urlpatterns = [
    path('', views.seznam_ukolu, name='seznam_ukolu'),
]
