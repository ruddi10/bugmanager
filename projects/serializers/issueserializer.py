from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from projects.models import Issue, IssueAssign
from rest_framework import serializers

User = get_user_model()


class AssignSerializer(serializers.ModelSerializer):
    # assigned_to = serializers.CharField(source='assigned_to.username')
    # assigned_by = serializers.CharField(source='assigned_by.username')

    class Meta:
        model = IssueAssign
        fields = ('assigned_to', 'assigned_by')


class IssueSerializer(serializers.ModelSerializer):
    reporter = serializers.ReadOnlyField(source='reporter.username')
    assigned = AssignSerializer(read_only=True)
   # team = TeamSerializer(many=True)
    # team = serializers.SlugRelatedField(
    #     many=True,
    #     queryset=User.objects.all(),
    #     slug_field='username',

    # )

    class Meta:
        model = Issue
        fields = ('project', 'heading', 'reporter', 'assigned',
                  'description', 'tags', 'status')
        read_only_fields = ('assigned', 'reporter', 'status')
    # def create(self, validated_data):
    #     team = validated_data.pop('team')
    #     project = Project.objects.create(**validated_data)
    #     for member in team:
    #         project.team.add(member)
    #     project.team.add(project.creator)
    #     return project


class IssueUpdateSerializer(serializers.ModelSerializer):
    reporter = serializers.ReadOnlyField(source='reporter.username')
    assigned = AssignSerializer()
   # team = TeamSerializer(many=True)
    # team = serializers.SlugRelatedField(
    #     many=True,
    #     queryset=User.objects.all(),
    #     slug_field='username',

    # )

    class Meta:
        model = Issue
        fields = ('project', 'heading', 'reporter', 'assigned',
                  'description', 'tags', 'status')
        read_only_fields = ('heading', 'reporter', 'description', 'project')
