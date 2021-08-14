from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

# this wan't run on creating superuser
@receiver(post_save, sender=User)
def save_profile(sender, created, instance, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()
        