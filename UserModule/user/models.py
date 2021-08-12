from typing import Tuple
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.base import Model


class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        # We need to add args if we have assinged to our custom-user model. i.e username


        if not email:
            raise ValueError("You must have an email address")
        # if not username:
        #     raise ValueError("Users must have an username")

        user = self.model(
            email = self.normalize_email(email),
            # username = username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        # We need to add args if we have assinged to our custom-user model. i.e username

        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            # username = username
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user



class User(AbstractBaseUser):
    # This are the fields that we define by our choice
    email = models.EmailField(verbose_name='email', max_length=150, unique=True)
    # username = models.CharField(max_length=50)

    # This fields are compulsion 
    date_joined = models.DateTimeField(verbose_name='date joined' ,auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    # is_admin = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=True) # whether this user account should be considered active
    is_staff = models.BooleanField(default=False) #  whether this user can access the admin site.
    is_superuser = models.BooleanField(default=False) # this user has all permissions without explicitly assigning them.

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email' 
    # It replaces the built-in username field for whatever you designate. 
    # In this case, we decided to opt for an EmailField but you can also consider using a phone number.


    REQUIRED_FIELDS = [] # Email & Password are required by default.
    # if we use username field then we need add that field to REQUIRED_FIELDS

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    objects = UserManager()

# Don't forget to add this custom-model in settings.py file as AUTH_USER_MODEL = 'user.user'
# So what to use? get_user_model accounts.models.User or what? 
# Actually, you'll use settings.AUTH_USER_MODEL every time 
# regardless of user model customiation

"""
This is not a class, but demo verison to get custom-user-model

from django.conf import settings

User = settings.AUTH_USER_MODEL
class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

or
from django.contrib.auth import get_user_model

User = get_user_model()

"""