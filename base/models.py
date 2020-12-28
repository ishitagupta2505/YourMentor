from colorfield.fields import ColorField
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Course(models.Model):
	Code = models.CharField(max_length=10, null=True)
	Name = models.CharField(max_length=50, null=True)
	Coordinator = models.CharField(max_length=50, null=True, blank=True)
	color = ColorField(default='#ffffff')

	def __str__(self):
		return self.Code


class Student(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	UserName = models.CharField(max_length=50, null=True)
	RollNo = models.IntegerField(null=True)
	Email = models.EmailField(max_length=100, unique=True, null=True)
	Year_of_study = models.IntegerField(null=True)
	Department = models.CharField(max_length=200, null=True)
	CoursesEnrolled = models.ManyToManyField(Course)
	Password = models.CharField(max_length=20, null=True)
	profile_pic = models.ImageField(null=True, blank=True)

	def __str__(self):
		return str(self.user)

class Teacher(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	UserName = models.CharField(max_length=100, null=True)
	Designation = models.CharField(max_length=100, null=True)
	Department = models.CharField(max_length=200, null=True)
	Email = models.EmailField(max_length=100, unique=True, null=True)
	Special = models.TextField()
	CoursesEnrolled = models.ManyToManyField(Course)
	Password = models.CharField(max_length=20, null=True)
	profile_pic = models.ImageField(null=True, blank=True)

	def __str__(self):
		return str(self.user)
