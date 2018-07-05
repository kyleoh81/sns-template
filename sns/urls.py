from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("sns.api.urls", namespace="api")),
    path("", include("sns.status.urls", namespace="status")),
    path("", include("sns.profiles.urls", namespace="profiles")),
]

