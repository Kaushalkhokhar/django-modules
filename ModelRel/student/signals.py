from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import StudentResult

@receiver(post_delete, sender=StudentResult)
def delete_student(sender, instance, **kwargs):
    print('Post signla runs........')
    instance.student.delete()