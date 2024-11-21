"""
URL configuration for project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from application import views
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name= 'index'),
    path('contact/', views.contact, name= 'contact'),
    path('edit/<int:id>/', views.edit, name= 'edit'),
    path('delete/<int:id>/', views.delete, name= 'delete'),
    path('studentsapi/', views.studentsapi, name= 'studentsapi'),
    path('coursesapi/', views.coursesapi , name='coursesapi'),
    path('mpesaapi/', views.mpesaapi , name='mpesaapi'),
    path('about/', views.about, name='about'),  # Updated to use about_view
    path('edit_course/<int:id>/', views.edit_course, name='edit_course'),
    path('delete_course/<int:id>/', views.delete_course, name='delete_course'),



]


