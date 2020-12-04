from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from .forms import FacultyForm, StudentForm

# Create your views here.
from .models import *


from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users
from django.db.models import Q




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

			group = Group.objects.get(name='student')
			user.groups.add(group)
			Student.objects.create(
				user=user,)

			messages.success(request, 'Student registered successfully with username: ' + username)

	context = {'form': form}
	return render(request, 'base/register.html', context)
	

@allowed_users(allowed_roles=['admin'])
def registerTeacher(request):

	form = UserCreationForm()

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
		
			group = Group.objects.get(name='teacher')
			user.groups.add(group)
			Teacher.objects.create(
				user=user,)

			messages.success(request, 'Teacher registered successfully with username: ' + username)


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
	return redirect('home')


@login_required(login_url='login')
def department(request):
	return render(request, 'base/department.html')


@login_required(login_url='login')
def mycourse(request):
	courses = Course.objects.filter(student__user=request.user)
	coursesteacher = Course.objects.filter(teacher__user=request.user)

	context = {'courses': courses, 'coursesteacher': coursesteacher}
	return render(request, 'base/course.html', context)


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


@login_required(login_url='login')
def teacherlist(request, department):

    t = Teacher.objects.filter(Department=department)
    
    context={'t': t}
    return render(request, 'base/teacherlist.html', context)


@login_required(login_url='login')
def courseteachers(request, courses):
	t = Teacher.objects.filter(CoursesEnrolled__Name=courses)
	context={'t': t}
	return render(request, 'base/teacherlist.html', context)

@login_required(login_url='login')
def accountSettings(request):
	teacher = request.user.teacher
	form = FacultyForm(instance=teacher)

	if request.method == 'POST':
		form = FacultyForm(request.POST, request.FILES, instance=teacher)
		if form.is_valid():
			form.save()

			return redirect('/')


	context = {'form':form}
	return render(request, 'base/edit.html', context)


@login_required(login_url='login')
def accountSettingsstudent(request):
	student = request.user.student
	form = StudentForm(instance=student)

	if request.method == 'POST':
		form = StudentForm(request.POST, request.FILES, instance=student)
		if form.is_valid():
			form.save()

			return redirect('/')


	context = {'form':form}
	return render(request, 'base/edit.html', context)


@login_required(login_url='login')
def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        print(query)

        submitbutton= request.GET.get('submit')
        print(submitbutton)

        if query is not None:
            lookups= Q(UserName__icontains=query)

            results= Teacher.objects.filter(lookups)
            resultsstudent = Student.objects.filter(lookups)
            print(results)
            print(resultsstudent)

            context={'results': results, 'resultsstudent':resultsstudent, 
                     'submitbutton': submitbutton}

            return render(request, 'base/search.html', context)

        else:
            return render(request, 'base/search.html')

    else:
        return render(request, 'base/search.html')

