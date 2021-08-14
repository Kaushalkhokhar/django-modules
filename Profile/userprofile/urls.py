from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_update, name='update-profile'),
    path('home/', views.home, name='home'),
]