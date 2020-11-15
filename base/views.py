from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *


from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
	return render(request, 'base/home.html')


def about(request):
	return render(request, 'base/about.html')


def loginUser(request):
	if request.user.is_authenticated:
		return redirect('department')
	else:
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