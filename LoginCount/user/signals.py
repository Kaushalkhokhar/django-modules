from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.cache import cache
User = get_user_model()

@receiver(user_logged_in, sender=User)
def count_on_login(sender, request, user, **kwargs):
    c = cache.get('count', 0, version=user.pk)
    c += 1
    cache.set('count', c, 60*60*24, version=user.pk)
    print(10*'%%')
    print(c)