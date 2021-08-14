from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate
from django.contrib import messages
from django.core.cache import cache

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



@login_required
def home(request):
    c = cache.get('count', version=request.user.pk)
    return HttpResponse(f"login count: {c}")

@login_required
def logout(request):
    auth_logout(request)
    return HttpResponse('Log out success')