from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register_form/', views.register_form, name='register_form'),
    path('register_form/login_form', views.login_form, name='login_form'),
    path('register_form/register_form', views.register_form, name='register_form'),
    path('register_form/register', views.register, name='register'),
    path('login_form/', views.login_form, name='login_form'),
    path('login_form/login_form', views.login_form, name='login_form'),
    path('login_form/register_form', views.register_form, name='register_form'),
    path('login_form/loginuser', views.loginuser, name='loginuser'),
    path('login_form/register', views.register, name='register'),
    path('restaurant/<str:slug>/<str:name>', views.restaurant, name='restaurant'),
    path('register/', views.register, name='register'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('logutuse', views.logoutuser, name='logoutuser'),
]

#regex google search.