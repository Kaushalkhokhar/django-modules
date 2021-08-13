from django.urls import path
from . import views
urlpatterns = [
    path('set/',  views.set, name='set'),
    path('get/',  views.get, name='get'),
    path('del/',  views.delt, name='del'),
]