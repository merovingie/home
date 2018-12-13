from django.urls import path
from . import views
from jobs import views as jobs_views

urlpatterns = [
    path('logout', views.logout, name= 'logout'),
    path('login', views.login, name= 'login'),
    path('', jobs_views.jobs, name= 'home'),
    ]