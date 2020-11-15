from django.contrib import admin

# Register your models here.

from .models import *
# * to import all models


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ('Code', 'Name')
	search_fields = ('Code', 'Name')


#admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
