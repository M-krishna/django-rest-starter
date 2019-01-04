"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from webapp import views
from student.views import StudentView 
from Authentication.views import SignUpView
from todo.views import TodoView, GetOneTodoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', StudentView.as_view()),
    path('employess/', views.EmployeeView.as_view()),
    path('signup/', SignUpView.as_view()),
    path('addtodo/', TodoView.as_view()),
    path('addtodo/<int:pk>', GetOneTodoView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]
