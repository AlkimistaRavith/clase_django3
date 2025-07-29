from django.urls import path
from mi_app import views

urlpatterns = [
    path('home/', views.home, name='home'),  # ✅ Primero va el patrón de URL como string
]


""" 
from django.urls import path
from .views import home

urlpatterns = [
    path("home/", views.home, name=home),
] """