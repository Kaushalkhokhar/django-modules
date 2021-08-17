from django.contrib import admin
from .models import Student, StudentResult, ResultColor, Subject, Teacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']
    ordering = ['id']

@admin.register(StudentResult)
class StudentResultAdmin(admin.ModelAdmin):
    list_display = ['pk', 'student', 'marks']
    ordering = ['pk']


@admin.register(ResultColor)
class ResultColorAdmin(admin.ModelAdmin):
    list_display = ['result', 'color']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'student_list']