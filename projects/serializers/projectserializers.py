from rest_framework import serializers
from projects.models import Projectmodel
from django.contrib.auth.models import User


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class ProjectSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
   # team = TeamSerializer(many=True)
    team = serializers.SlugRelatedField(
        many=True,
        queryset=User.objects.all(),
        slug_field='username',

    )

    class Meta:
        model = Projectmodel.Project
        fields = ('title', 'team', 'creator', 'wiki', 'createdAt')

    def create(self, validated_data):
        team = validated_data.pop('team')
        project = Projectmodel.Project.objects.create(**validated_data)
        for member in team:
            project.team.add(member)
        project.team.add(project.creator)
        return project
