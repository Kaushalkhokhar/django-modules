from django.contrib import admin
from .models import Student, ProxyStudent

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']
    ordering = ['id']

@admin.register(ProxyStudent)
class ProxyStudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']
