from django.shortcuts import render, HttpResponse
from .models import Student, ProxyStudent


def home(request):
    std_dms = Student.objects.all()
    std_cms = Student.students.all()
    # our custom name of manager as student
    for std in std_dms:
        print(std)

    print('#########################')
    print('#########################')

    for std in std_cms:
        print(std)

    print('#########################')
    print('#########################')

    std_by_age = Student.students.get_by_age_range(12, 14)

    for std in std_by_age:
        print(std)


    print('#########################')
    print('#########################')

    std_ps = ProxyStudent.pStudents.get_by_age_range(13, 15)
    
    for std in std_ps:
        print(std)


    return HttpResponse('See in terminal....')
