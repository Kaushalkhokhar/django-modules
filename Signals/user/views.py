from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.forms import AuthenticationForm


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Login Success')
    else:
        form = AuthenticationForm()

    return render(request, 'user/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')

def home(request):
    a = 10/0
    return HttpResponse('Hello')