from django.urls import path
from . import views
urlpatterns = [
    path('signup', views.signUpPage, name='signup_page'),
    path('api/signup', views.signUp, name='signup'),
    path('login', views.logInPage, name='login_page'),
    path('api/login', views.logIn, name='login'),
    path('api/logout', views.logOut, name='logout'),
]

