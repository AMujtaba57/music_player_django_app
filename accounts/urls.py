from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("Signup/", views.SignupPage, name="SignupPage"),
    path('logout/', views.logoutPage, name='logout'),

    path('home/', views.home, name='home'),
]