# Name: bansri shah
# course: CST8333 Programming Language Research Project.
# Assignment 3
# student-number: 040920837
"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include,re_path


print("Bansri shah")
urlpatterns = [
    path('admin/', admin.site.urls),
    # this function re_path returns element in urls patterns format in which we pass include paramter means it include another file urls
    re_path('', include('myapplication.urls')),

]
