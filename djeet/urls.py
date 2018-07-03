from django.urls import path
from django.views.generic.base import TemplateView

from .views import FeedView
from .apps import app_name


urlpatterns = [
    path("feed/", FeedView.as_view(), name="feed"),
]
