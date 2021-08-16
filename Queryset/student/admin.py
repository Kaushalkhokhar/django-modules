from django.contrib import admin
from .models import Students, Teachers 


@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll_no', 'marks', 'city', 'pass_date']

@admin.register(Teachers)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'salary', 'city', 'join_date']
