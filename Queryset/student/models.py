from django.db import models
from datetime import datetime

class Students(models.Model):
    name = models.CharField(max_length=25)
    roll_no = models.IntegerField()
    marks = models.IntegerField()
    city = models.CharField(max_length=25)
    pass_date = models.DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return self.name


class Teachers(models.Model):
    name = models.CharField(max_length=25)
    salary = models.IntegerField()
    city = models.CharField(max_length=25)
    join_date = models.DateTimeField()


    def __str__(self):
        return self.name