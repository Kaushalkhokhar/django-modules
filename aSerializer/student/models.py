from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    pass_date = models.DateTimeField()