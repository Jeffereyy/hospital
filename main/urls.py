from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", auth_views.LoginView.as_view(template_name = "main/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name = "main/logout.html"), name="logout"),
    path("doctors/", views.doctors, name="doctors"),
    path("doctors/<str:doctor_name>", views.Book.as_view(), name="book"),
]