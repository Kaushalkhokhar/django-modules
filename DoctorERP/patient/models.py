from django.db import models
from user.models import UserWithMoreFields
from doctor.models import Doctor

class Patient(UserWithMoreFields):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    