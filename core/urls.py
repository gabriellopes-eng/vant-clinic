from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, register

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("auth/login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("auth/register/", register, name="register"),
]
