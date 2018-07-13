import os

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Status
from .apps import app_name


def app_path(file_name):
    return os.path.join(app_name, file_name)


class FeedView(TemplateView, LoginRequiredMixin):
    template_name = app_path("statuses.html")

    def get(self, request):
        userids = [item.id for item in request.user.profile.follows.all()]
        userids.append(request.user.id)
        statuses = list(Status.objects.filter(user_id__in=userids)[:25])
        return self.render_to_response({
            "title": "Feed",
            "statuses": statuses,
            "url_statuses": "/api/feed/",
        })

