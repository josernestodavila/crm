from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path

urlpatterns = [
    path("", include("app.urls")),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("admin/", admin.site.urls),
]
