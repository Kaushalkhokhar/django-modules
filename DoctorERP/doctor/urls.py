from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='doctor-register'),
    path('login/', views.login, name='doctor-login'),
    path('home/', views.home, name='doctor-home'),
    path('patient_detail/<int:pk>/', views.patient_detail, name='patient-detail'),
]