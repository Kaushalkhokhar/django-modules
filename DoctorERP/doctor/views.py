from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import RegisterDoctorForm
from .models import Doctors
from user.forms import LoginForm
from patient.models import Patient



def register(request):
    if request.method == 'POST':
        form = RegisterDoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor-login')
    else:

        form = RegisterDoctorForm()

    return render(request, 'doctor/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('doctor-home')
    else:
        form = LoginForm()
    return render(request, 'doctor/login.html', {'form': form})

def home(request, pID=None):
    if not request.user.is_authenticated:
        return redirect('doctor-login')
    doctor = Doctors.objects.filter(email=request.user.email).first()
    all_p = doctor.patient_set.all()

    return render(request, 'doctor/home.html', {'all_p': all_p})

def patient_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('doctor-login')
    patient = Patient.objects.filter(id=pk).first()

    return render(request, 'doctor/patient-detail.html', {'patient': patient})
