from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='patient-register'),
    path('login/', views.login, name='patient-login'),
    path('home/', views.home, name='patient-home'),
]