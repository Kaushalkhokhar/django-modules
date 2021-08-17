from django.shortcuts import render, HttpResponse
from .models import StudentResult, Student, Teacher, Subject



def home(request):
    # subject has ManyToOne relationship with student
    """
    Getting student by filtering on subject
    """
    stds = Student.objects.all()

    # to get student related to subject as manytoone relationship
    std_by_sub = Student.objects.filter(subject__subject__icontains='maths')
    # here first subject is table name to which it is related
    # second subject if field name
    # third as we know is lookup

    # to get student related to teacher as manytomany relationship
    std_by_tech = Student.objects.filter(teacher__name__icontains='paresh')

    for std in std_by_sub:
        print(std)

    print(10*'%%')

    for std in std_by_tech:
        print(std)


    """
    Getting subject by filtering on student
    """
    sub_by_std = Subject.objects.filter(student__name='Riya')

    print(10*'%%')

    for sub in sub_by_std:
        print(sub)

    return HttpResponse('See in the terminal......')