from django.urls import path
from . import views

urlpatterns = [
    path("register",views.register, name='register'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path("dest_visit", views.dest_visit, name='dest_visit'),
    path("medu", views.medu, name='medu')
]
