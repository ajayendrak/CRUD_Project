from django.contrib import admin
from django.urls import path
from student_app import views

urlpatterns = [
    path('', views.std, name='std'),
    path('show', views.show, name='show'),
    path('delete<int:sid>', views.delete, name='delete'),
    path('update<int:sid>', views.update, name='update'),
    
]
