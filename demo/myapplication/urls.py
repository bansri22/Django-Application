# Name: bansri shah
# course: CST8333 Programming Language Research Project.
# Assignment 4
# student-number: 040920837
from django.urls import re_path
from .import views

print("Bansri shah")
urlpatterns = [
    re_path(r'^$',views.show,name='home'),
    re_path(r'^show',views.index, name='show'),
    re_path(r'^home', views.show, name='home'),
    re_path(r'^add', views.add, name='add'),
    re_path(r'^delete', views.delete, name='delete'),
    re_path(r'^updated', views.updated, name='updated'),
    re_path(r'^update', views.update, name='update'),
    re_path(r'^data', views.data, name='data'),

]
