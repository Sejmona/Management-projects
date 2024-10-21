from django.urls import path
from . import views

urlpatterns = [
    path('', views.seznam_ukolu, name='seznam_ukolu'),
    path('novy/', views.pridat_ukol, name='pridat_ukol'),
    path('edit/<int:pk>/', views.edit_ukol, name='edit_ukol'),
    path('smazat/<int:pk>/', views.smazat_ukol, name='smazat_ukol'),
]
