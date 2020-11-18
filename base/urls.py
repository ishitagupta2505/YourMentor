from django.urls import path
from . import views

urlpatterns=[

	path('', views.home, name="home"),
	path('about/', views.about, name="about"),
	path('register/', views.registerUser, name="register"),
	path('registerTeacher/', views.registerTeacher, name="registerTeacher"),
	path('login/', views.loginUser, name="login"),
	path('logout/', views.logoutUser, name="logoutUser"),
	path('department/', views.department, name="department"),
	path('mycourse/', views.mycourse, name="mycourse"),
	path('profilestudent/', views.profilestudent, name="profilestudent"),
	path('profileteacher/', views.profileteacher, name="profileteacher"),

]