from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm


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

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('login')
        
    if request.method == 'POST':
        # with old password
        form = PasswordChangeForm(user=request.user, data=request.POST)
        # without old password
        # form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        form = PasswordChangeForm(user=request.user)
        # form = SetPasswordForm(user=request.user, data=request.POST)


    return render(request, 'user/change-password.html', {'form': form})
    

def logout(request):
    auth_logout(request)
    return redirect('login')