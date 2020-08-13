from django.urls import path
from . import views


urlpatterns = [
    path('', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('signup_again', views.signup_again, name="signup_again")
]