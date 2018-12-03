from django.urls import path
from . import views
#from login import views as views_login

urlpatterns = [
    path('', views.jobs, name= 'jobs'),
#    path('histo/', views_login.index, name ='histo'),
    ]