from django.contrib import admin

# Register your models here.

from .models import *
# * to import all models


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ('Code', 'Name')
	search_fields = ('Code', 'Name')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
	list_display = ('UserName', 'Email')
	search_fields = ('UserName', 'Email')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('UserName', 'Email')
	search_fields = ('UserName', 'Email')


