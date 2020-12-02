from django.forms import ModelForm
from django import forms

from .models import *

class FacultyForm(ModelForm):
	class Meta:
		model = Teacher
		fields = '__all__'
		exclude = ['user']


class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = '__all__'
		exclude = ['user']