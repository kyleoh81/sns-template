import django_filters

from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

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

    @action(methods=["get"], detail=True)
    def likes(self, request, pk=None):
        """Return a list of statuses liked by given user."""
        profile = self.get_object()
        likes_qs = profile.likes.all()
        likes = StatusSerializer(likes_qs, many=True).data
        return Response(likes)


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    @action(methods=["put"], detail=True)
    def like(self, request, pk=None):
        """Register a status with like."""
        status = self.get_object()
        request.user.profile.likes.add(status)
        status_data = StatusSerializer(status).data
        return Response(status_data)

    @action(methods=["delete"], detail=True)
    def stop_like(self, request, pk=None):
        """Register a status with like."""
        status = self.get_object()
        request.user.profile.likes.remove(status)
        status_data = StatusSerializer(status).data
        return Response(status_data)

   
