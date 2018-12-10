from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name= 'todo'),
    path('json/', views.jsontojs, name= 'json'),
    ]