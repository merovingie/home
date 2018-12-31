from django.urls import path
from . import views
# from Histologin import views as views_histologin

urlpatterns = [
    path('', views.index, name= 'index'),
    path('box_started/', views.box_started, name= 'box_started'),
    # path('kathy/', views_histologin.kathy, name= 'kathy'),
    path('box_details/<box_id>', views.box_details, name= 'box_details')
]