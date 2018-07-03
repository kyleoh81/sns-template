import django_filters
from rest_framework import viewsets, filters

from sns.profiles.models import Profile
from sns.status.models import Status
from sns.users.models import User
from .serializer import ProfileSerializer, StatusSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

