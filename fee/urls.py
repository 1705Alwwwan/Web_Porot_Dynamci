from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path ('register/', views.my_register, name='my-register'), 
    path ('login/', views.my_login, name='my-login'), 
    path('logout/', views.my_logout, name='my-logout'), 
    
]