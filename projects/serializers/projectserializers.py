from rest_framework import serializers
from projects.models import Project
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .issueserializer import IssueSerializer

User = get_user_model()


class ProjectSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    team = serializers.SlugRelatedField(
        many=True,
        queryset=User.objects.all(),
        slug_field='username',

    )

    class Meta:
        model = Project
        fields = ('id', 'title', 'team', 'creator', 'wiki', 'createdAt')
        read_only_fields = ('id', 'creator')

    def create(self, validated_data):
        team = validated_data.pop('team')
        project = Project.objects.create(**validated_data)
        for member in team:
            project.team.add(member)
        project.team.add(project.creator)
        return project


class ProjectDetailSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    team = serializers.SlugRelatedField(
        many=True,
        queryset=User.objects.all(),
        slug_field='username',

    )
    bugs = IssueSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'team', 'creator',
                  'wiki', 'createdAt', 'bugs')
        read_only_fields = ('id', 'creator', 'createdAt')
