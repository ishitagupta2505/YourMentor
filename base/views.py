from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def home(request):
	return HttpResponse('<h1>home</h1>')

def about(request):
	return HttpResponse('<h1>about</h1>')

def login(request):
	return HttpResponse('<h1>login</h1>')
