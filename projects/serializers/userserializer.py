from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from projects.models import Issue, Tag, Comment, Profile
from rest_framework import serializers, fields
from projects.constants import *

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'is_superuser', 'profile')
