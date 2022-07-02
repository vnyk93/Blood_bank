from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),    
    path('register',views.register),    
    path('login',views.login),
    path('contact',views.contact),
    
    path('usersave',views.usersave),
    path('userlogin',views.userlogin),

    path('user/home',views.userhome),
    path('user/request',views.bloodrequest),
    path('user/saverequest',views.saverequest),
    path('logout',views.logout),
]
