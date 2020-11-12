from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request, 'base/home.html')

def about(request):
	return render(request, 'base/about.html')

def login(request):
	return HttpResponse('<h1>login</h1>')
