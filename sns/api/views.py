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

    @action(detail=True)
    def likes(self, request, pk=None):
        """Return a list of statuses liked by given user."""
        profile = self.get_object()
        likes = profile.likes.all()
        result = StatusSerializer(likes, many=True).data
        return Response(result)

    @action(detail=True)
    def statuses(self, request, pk=None):
        """Return statuses user posted."""
        profile = self.get_object()
        statuses = profile.user.statuses.order_by("-created_at")
        result = StatusSerializer(statuses, many=True).data
        return Response(result)


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        """Return feed."""
        userids = [item.id for item in request.user.profile.follows.all()]
        userids.append(request.user.id)
        statuses = Status.objects.filter(user_id__in=userids).order_by("-created_at")[:25]
        result = self.get_serializer_class()(statuses, many=True).data
        return Response(result)
               


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def manage_relation(self, request, op):
        """Resiter/Remove status with likes."""
        status = self.get_object()
        getattr(request.user.profile.likes, op)(status)
        serializer = self.get_serializer_class()
        result = serializer(status).data
        return Response(result)
 
    def update(self, request, pk=None):
        """Resister status with likes."""
        return self.manage_relation(request, "add")

    def delete(self, request, pk=None):
        """Remove status from likes."""
        return self.manage_relation(request, "remove")


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def manage_relation(self, request, op):
        """Follow/Unfollow user."""
        profile = self.get_object()
        getattr(request.user.profile.follows, op)(profile)
        serializer = self.get_serializer_class()
        result = serializer(profile).data
        return Response(result)
 
    def update(self, request, pk=None):
        """Follow user."""
        return self.manage_relation(request, "add")

    def delete(self, request, pk=None):
        """Unfollow user."""
        return self.manage_relation(request, "remove")

