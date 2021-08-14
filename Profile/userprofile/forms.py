from django.contrib.auth import get_user_model
from django import forms
from .models import Profile
User = get_user_model()

class UserUpdateForm(forms.ModelForm):
   class Meta:
        model = User
        fields = ['email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['img']