from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Doctor(User):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def get_full_name(self):
        # The user is identified by their first_name last_name
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        # The user is identified by their first_name
        return self.first_name