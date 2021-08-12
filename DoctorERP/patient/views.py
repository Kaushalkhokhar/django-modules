from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import RegisterPatientForm
from user.forms import LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterPatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient-login')
    else:

        form = RegisterPatientForm()

    return render(request, 'patient/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('patient-home')
    else:
        form = LoginForm()
    return render(request, 'patient/login.html', {'form': form})

def home(request, pID=None):
    if not request.user.is_authenticated:
        return redirect('doctor-login')

    return render(request, 'patient/home.html')