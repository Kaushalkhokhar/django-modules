from django import forms
from django.db import models
from django.forms import fields, widgets
from doctor.models import Doctors
from .models import Patient
from user.forms import UserAdminCreationForm

class RegisterPatientForm(UserAdminCreationForm):
    doctor = forms.ModelChoiceField(queryset=Doctors.objects.all())

    class Meta(UserAdminCreationForm.Meta):
        model = Patient
        fields = ['email', 'first_name', 'last_name', 'doctor']

# One important point to be noted here:
# only those fields are saved to the model which is defined as fields in meta class
# otherwise, it displayed as a form but wan't save to model