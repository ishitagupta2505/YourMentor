from django.urls import path
from . import views

urlpatterns=[

	path('', views.home, name="home"),
	path('about/', views.about, name="about"),
	path('login/', views.loginUser, name="login"),
	path('logout/', views.logoutUser, name="logoutUser"),
	path('department/', views.department, name="department"),
	path('mycourse/', views.mycourse, name="mycourse"),

]