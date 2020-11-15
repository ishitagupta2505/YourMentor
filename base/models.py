from django.db import models

# Create your models here.

class Course(models.Model):
	Code = models.CharField(max_length=10, null=True)
	Name = models.CharField(max_length=50, null=True)
	Coordinator = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.Code

class Student(models.Model):
	UserName = models.CharField(max_length=50, null=True)
	RollNo = models.IntegerField(null=True)
	Email = models.EmailField(max_length=100, unique=True, null=True)
	Year_of_study = models.IntegerField(null=True)
	Department = models.CharField(max_length=10, null=True)
	Courses_enrolled = models.ManyToManyField(Course)
	Password = models.CharField(max_length=10, null=True)

	def __str__(self):
		return self.UserName

class Teacher(models.Model):
	UserName = models.CharField(max_length=50, null=True)
	Teacher_code = models.IntegerField(null=True)
	Email = models.EmailField(max_length=100, unique=True, null=True)
	Special = models.TextField()
	Courses_enrolled = models.ManyToManyField(Course)
	Password = models.CharField(max_length=10, null=True)

	def __str__(self):
		return self.UserName