from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render
from .forms import UserAdminCreationForm


def register(request):
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            group = Group.objects.get(name='normal')
            user = form.save()
            user.groups.add(group)
            import pdb
            pdb.set_trace()
            return redirect('login')
    else:
        form = UserAdminCreationForm()

    return render(request, 'user/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')

    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})  

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.user.has_perm('user.delete_user'):
        print(10* '%%')
        print('Has permission to delete user')
    
    # prints all the permission given to that user
    pr = request.user.get_all_permissions()
    print(pr)

    return render(request, 'user/home.html', {'user': request.user})

def logout(request):
    auth_logout(request)
    return redirect('login')