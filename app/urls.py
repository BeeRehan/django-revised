from django.contrib import admin
from django.urls import path
from django.views import View
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('add/',views.add, name='add'),
    path('mark_finished/<int:pk>',views.finshed, name='mark_finished'),
    path('mark_edit/<int:pk>',views.edit, name='mark_finished'),
    path('mark_delete/<int:pk>',views.delete, name='mark_finished'),
]
