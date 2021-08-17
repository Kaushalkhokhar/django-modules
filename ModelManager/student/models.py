from django.db import models



# custom manager
class StudentManager(models.Manager):
    # this method overrides the default method in manager class
    def get_queryset(self): # it runs when we call all()
        return super().get_queryset().order_by('name')


    # adding extra method to our manager
    def get_by_age_range(relf, r1, r2):
        return super().get_queryset().filter(age__range=(r1, r2))

class Student(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    # to change the manager name
    objects = models.Manager() # it is default
    students = StudentManager()

class ProxyStudent(Student):

    """
    Here this model just chages the python behaviour of student model
    """

    pStudents = StudentManager()
    class Meta:
        proxy = True
        ordering = ['age']