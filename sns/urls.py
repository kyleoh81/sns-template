from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

from sns.api.urls import router as api_router


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_router.urls)),
    path("", include("sns.status.urls", namespace="status")),
    path("", include("sns.profiles.urls", namespace="profiles")),
]

