from django.contrib import admin
from .models import Student, Teacher, Contractor, Car, CarColor, Toys, MyToys

@admin.register(Student)
class StudentAmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'marks']

@admin.register(Teacher)
class TeacherAmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'salary', 'date']

@admin.register(Contractor)
class ContractorAmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'salary', 'date']

@admin.register(Car)
class CarAmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'company']

@admin.register(CarColor)
class CarColorAmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'company', 'color']

@admin.register(Toys)
class ToysAmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']

@admin.register(MyToys)
class MyToysAmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']