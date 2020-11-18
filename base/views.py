from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .models import *


from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users



def home(request):
	return render(request, 'base/home.html')


def about(request):
	return render(request, 'base/about.html')

@allowed_users(allowed_roles=['admin'])
def registerUser(request):

	form = UserCreationForm()

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'User registered successfully with username: ' + username)

			group = Group.objects.get(name='student')
			user.groups.add(group)
			Student.objects.create(
				user=user,)

	context = {'form': form}
	return render(request, 'base/register.html', context)
	

@allowed_users(allowed_roles=['admin'])
def registerTeacher(request):

	form = UserCreationForm()

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			userteacher = form.save()
			userteachername = form.cleaned_data.get('username')
			messages.success(request, 'User registered successfully with username: ' + userteachername)

			group = Group.objects.get(name='teacher')
			userteacher.groups.add(group)
			Teacher.objects.create(
				user=user,)

	context = {'form': form}
	return render(request, 'base/register.html', context)


@unauthenticated_user
def loginUser(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('department')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'base/login.html', context)



def logoutUser(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect('login')


@login_required(login_url='login')
def department(request):
	return render(request, 'base/department.html')


@login_required(login_url='login')
def mycourse(request):
	return render(request, 'base/course.html')


@login_required(login_url='login')
# @allowed_users(allowed_roles=['student'])
def profilestudent(request):
	courses = Course.objects.filter(student__user=request.user)
	count = courses.count()

	s = Student.objects.get(user=request.user)

	context = {'courses':courses, 's':s, 'count':count}
	return render(request, 'base/profilestudent.html', context)


@login_required(login_url='login')
# @allowed_users(allowed_roles=['teacher'])
def profileteacher(request):
	courses = Course.objects.filter(teacher__user=request.user)
	count = courses.count()
	
	t = Teacher.objects.get(user=request.user)

	context = {'courses':courses, 't':t, 'count':count}
	return render(request, 'base/profileteacher.html', context)