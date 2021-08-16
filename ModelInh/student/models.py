from django.db import models
from django.db.models.fields import DateTimeField, proxy


"""
Abstract Base Inheritance
"""
class Commom(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True


class Student(Commom):
    marks = models.IntegerField()
    date = None # Will not make column


class Teacher(Commom):
    salary = models.IntegerField()
    date = DateTimeField() # will override

class Contractor(Commom):
    salary = models.IntegerField() 
    # will take default date field


"""
Multitable inheritance
"""

class Car(models.Model):
    name = models.CharField(max_length=25)
    company = models.CharField(max_length=25, choices=[('SK', 'Skoda'),
                                        ('VT', 'Vento'),
                                        ('AU', 'Audi'),
                                ])

    def __str__(self):
        return self.name

class CarColor(Car):
    color = models.CharField(max_length=25, choices=[('RD', 'Red'),
                                        ('BL', 'Blue'),
                                        ('YL', 'Yello'),
                                        ('WT', 'White'),
                                ])

    def __str__(self):
        return self.name + ' with ' + self.color

"""
Proxy model inheritance
"""

class Toys(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class MyToys(Toys):
    def __str__(self):
        return self.name + ' is of ' + str(self.price)

    class Meta:
        proxy = True
        ordering = ['price']

    # here just we have change the str and ordering of Toys
    # for such case we use proxy model