"""Serializer for rest api."""
from rest_framework import serializers

from sns.profiles.models import Profile
from sns.status.models import Status
from sns.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Provide serializer for user."""
    class Meta:
        model = User
        fields = ("username", "nickname")


class ProfileSerializer(serializers.ModelSerializer):
    """Provide serializer for profile."""
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ("user", "follows", "likes", )


class StatusSerializer(serializers.ModelSerializer):
    """Provide serializer for status."""
    user = UserSerializer()
    
    class Meta:
        model = Status
        fields = ("user", "body", "created_at")

