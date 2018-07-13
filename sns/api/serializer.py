"""Serializer for rest api."""
from rest_framework import serializers

from sns.profiles.models import Profile
from sns.status.models import Status
from sns.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Provide serializer for user."""

    class Meta:
        model = User
        fields = ("pk", "username", "nickname",)

    def get_is_me(self, obj):
        return False

class ProfileSerializer(serializers.ModelSerializer):
    """Provide serializer for profile."""
    user = UserSerializer()
    is_me = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ("pk", "user", "follows", "likes", "is_me")

    def get_is_me(self, obj):
        return False



class StatusSerializer(serializers.ModelSerializer):
    """Provide serializer for status."""
    user = UserSerializer()
    
    class Meta:
        model = Status
        fields = ("pk", "user", "body", "created_at")

