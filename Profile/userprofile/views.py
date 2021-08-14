from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, UserUpdateForm


@login_required
def profile_update(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,
                            request.FILES, 
                            instance=request.user.profile)

        u_form = UserUpdateForm(request.POST,
                                instance=request.user)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

    else:
        p_form = ProfileUpdateForm()        
        u_form = UserUpdateForm()

    return render(request, 'userprofile/profile_update.html', {'u_form': u_form, 'p_form': p_form})

@login_required
def home(request):
    return render(request, 'userprofile/home.html')