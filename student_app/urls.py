from django.contrib import admin
from django.urls import path
from student_app import views

urlpatterns = [
    path('', views.std, name='std'),
    path('show', views.show, name='show'),
    path('delete<int:id>', views.delete, name='delete'),
    path('update<int:id>', views.update, name='update'),
    
]
