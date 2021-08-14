from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed 
from django.db.models.signals import pre_save, post_save, pre_migrate, post_migrate, pre_delete, post_delete
from django.contrib.auth import get_user_model
from django.core.signals import request_finished, request_started, got_request_exception
from django.db.backends.signals import connection_created
from django.dispatch import receiver
User = get_user_model()


@receiver(user_logged_in, sender=User)
def login_success(sender, **kwargs):
    for s in sender.objects.all():
        print(s.id)
    print(kwargs) # we can see the args by seeing kwargs data
    print(kwargs.get('user'))

# user_logged_in.connect(login_success, sender=User)

# to work signals
# We need to add ready method in apps.py and default_app_config in __init__.py


# runs when user logs out
@receiver(user_logged_out, sender=User)
def logout_success(sender, **kwargs):
    print(sender)
    print(kwargs.get('user'))

# runs when login fails
@receiver(user_login_failed)
def login_failed(sender, **kwargs):
    print(sender)
    print(kwargs)

# runs before save method of model
@receiver(pre_save, sender=User)
def before_save_model(sender, **kwargs):
    print(10*'%%')
    print('Pre save method..........')
    print(sender)
    print(kwargs)

# runs after save method of model
@receiver(post_save, sender=User)
def after_save_model(sender, created, **kwargs):
    """
    here created parameter is true when new user created
    and false when user modified
    """
    print(10*'%%')
    print('Post save method..........')
    print(f'created: {created}')
    print(sender)
    print(kwargs)


# runs when HTTP request starts
@receiver(request_started)
def at_request_start(sender, **kwargs):
    print(10*'%%')
    print('Request started......')
    print(sender)
    print(kwargs)


# runs when HTTP request finish
@receiver(request_finished)
def at_request_finish(sender, **kwargs):
    print(10*'%%')
    print('Request finished......')
    print(sender)
    print(kwargs)

# runs when HTTP exception in request
# to test this make view to generate an exception
@receiver(got_request_exception)
def at_request_exception(sender, **kwargs):
    print(10*'%%')
    print('Request excepetion......')
    print(sender)
    print(kwargs)

# runs before migrate command
# this runs for every app
@receiver(pre_migrate)
def before_install_app(sender, **kwargs):
    print(10*'%%')
    print('Pre migrate......')
    print(sender)
    print(kwargs)

# runs at end of migrate
@receiver(post_migrate)
def after_install_app(sender, **kwargs):
    print(10*'%%')
    print('Post migrate......')
    print(sender)
    print(kwargs)

# runs at end of migrate
# it run when we we execute runserver command
@receiver(connection_created)
def conn_db(sender, **kwargs):
    print(10*'%%')
    print('Initial connection to the database......')
    print(sender)
    print(kwargs)
