from django.shortcuts import render, HttpResponse
from .models import Teacher, Student, Contractor, Car, CarColor, Toys, MyToys


def home(request):
    """
    Abstractbase Inheritance
    """
    stds = Student.objects.all()
    techs = Teacher.objects.all()
    cons = Contractor.objects.all()

    for std in stds:
        print(std)

    for tech in techs:
        print(tech)

    for con in cons:
        print(con)


    """
    Multitable inheritance
    """
    cars = Car.objects.all()
    carcs = CarColor.objects.all()

    print(10* '%%')

    for car in cars:
        print(car)

    for carc in carcs:
        print(carc)


    """
    Multitable inheritance
    """
    ts = Toys.objects.all()
    mts = MyToys.objects.all()

    print(10* '%%')

    for t in ts:
        print(t)

    for mt in mts:
        print(mt)

    return HttpResponse('See in terminal....')
