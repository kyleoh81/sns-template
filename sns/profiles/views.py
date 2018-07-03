import os

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView

from .forms import SignupForm, SigninForm
from .apps import app_name

from status.forms import StatusForm
from users.models import User
from status.models import Status


def app_path(file_name):
    return os.path.join(app_name, file_name)

def top_url():
    return reverse(f"{app_name}:frontpage")

def return_to_top():
    topurl = top_url()
    return redirect(topurl)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = app_path("profile.html")

    def get(self, request, username):
        context = {
            "user": get_object_or_404(User, username=username),
            "form": StatusForm()
        }
        return self.render_to_response(context)

    def post(self, request, username):
        user = get_object_or_404(User, username=username)
        form = StatusForm(data=request.POST)

        if form.is_valid():
            status = form.save(commit=False)
            status.user = user
            status.save()

        return self.render_to_response({ "form": form, "user": user, })


class FrontPageView(TemplateView):
    template_name = "sns/frontpage.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse(f"{app_name}:profile", args=[request.user.username]))
        
        signupform = SignupForm()
        signinform = SigninForm()

        context = {
            "signupform": signupform,
            "signinform": signinform
        }
        return self.render_to_response(context)

    def post(self, request):
        if 'signupform' in request.POST:
            signupform = SignupForm(data=request.POST)
            signinform = SigninForm()
    
            if signupform.is_valid():
                username = signupform.cleaned_data['username']
                password = signupform.cleaned_data['password1']
                signupform.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                return return_to_top()
   
        else:
            signinform = SigninForm(data=request.POST)
            signupform = SignupForm()
   
            if signinform.is_valid():
                login(request, signinform.get_user())
                return return_to_top()

        context = {
            "signupform": signupform,
            "signinform": signinform
        }
        return self.render_to_response(context)


class SignoutView(LogoutView):
    next_page = "/"


class FollowsView(TemplateView):
    template_name = app_path("users.html")

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        statuserprofiles = user.statuserprofile.follows.select_related("user").all()
        return self.render_to_response({
            "title": "Follows",
            "profiles": profiles,
        })


class FollowersView(TemplateView):
    template_name = app_path("users.html")

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        profiles = user.profile.followed_by.select_related("user").all()
        return self.render_to_response({
            "title": "Followers",
            "profiles": profiles,
        })

    
class FollowView(LoginRequiredMixin, TemplateView):
    
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        request.user.profile.follows.add(user.profile)
        return HttpResponseRedirect(reverse("{app_name}:profile", kwargs={"username": username}))


class StopFollowView(LoginRequiredMixin, TemplateView):
    
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        request.user.profile.follows.remove(user.statuserprofile)
        return HttpResponseRedirect(reverse("{app_name}:profile", kwargs={"username": username}))


class LikeView(LoginRequiredMixin, TemplateView):
    
    def get(self, request, status_id):
        status = get_object_or_404(Status, id=status_id)
        request.user.profile.likes.add(status)
        return redirect(request.META["HTTP_REFERER"])


class StopLikeView(LoginRequiredMixin, TemplateView):
    
    def get(self, request, status_id):
        status = get_object_or_404(Status, id=status_id)
        request.user.profile.likes.remove(status)
        return redirect(request.META["HTTP_REFERER"])


class LikesView(TemplateView):
    template_name = "status/statuss.html"

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        statuss = user.profile.likes.select_related("user").all()
        return self.render_to_response({
            "title": "Likes",
            "statuss": statuss,
        })


def page_not_found(request, template_name="404.html"):
    return render(request, template_name, {})

