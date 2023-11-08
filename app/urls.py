from django.urls import path

from sesame.views import LoginView

from . import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("login/", views.EmailLoginView.as_view(), name="email-login"),
    path("login/auth/", LoginView.as_view(), name="login"),
]
