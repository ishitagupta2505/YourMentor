from django.urls import path
from . import views

urlpatterns=[

	path('', views.home, name="home"),
	path('about/', views.about, name="about"),
	path('register/', views.registerUser, name="register"),
	path('registerTeacher/', views.registerTeacher, name="registerTeacher"),
	path('login/', views.loginUser, name="login"),

	# path('reset_password/',
 #     auth_views.PasswordResetView.as_view(template_name="base/password_reset.html"),
 #     name="reset_password"),

 #    path('reset_password_sent/', 
 #        auth_views.PasswordResetDoneView.as_view(template_name="base/password_reset_sent.html"), 
 #        name="password_reset_done"),

 #    path('reset/<uidb64>/<token>/',
 #     auth_views.PasswordResetConfirmView.as_view(template_name="base/password_reset_form.html"), 
 #     name="password_reset_confirm"),

 #    path('reset_password_complete/', 
 #        auth_views.PasswordResetCompleteView.as_view(template_name="base/password_reset_done.html"), 
 #        name="password_reset_complete"),

	path('logout/', views.logoutUser, name="logoutUser"),
	path('department/', views.department, name="department"),
	path('mycourse/', views.mycourse, name="mycourse"),
	path('profilestudent/', views.profilestudent, name="profilestudent"),
	path('profileteacher/', views.profileteacher, name="profileteacher"),
	path(r'^teachers/(?P<department>.+)/$', views.teacherlist, name="teachers"),
	path(r'^courseteachers/(?P<courses>.+)/$', views.courseteachers, name="courseteachers"),

]