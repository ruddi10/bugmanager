from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from projects.models import Issue, Tag, Comment
from rest_framework import serializers, fields
from projects.constants import *

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class CommentSerializer(serializers.ModelSerializer):
    # assigned_to = serializers.CharField(source='assigned_to.username')
    # assigned_by = serializers.CharField(source='assigned_by.username')
    commented_by = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',

    )
    comment_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Comment
        fields = ('comment_id', 'description', 'createdAt', 'commented_by')


class IssueSerializer(serializers.ModelSerializer):
    reporter = serializers.ReadOnlyField(source='reporter.username')
    assigned_by = UserSerializer(read_only=True)
    assigned_to = UserSerializer(read_only=True)
   # assigned = AssignSerializer(read_only=True)
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='tagname',

    )

    issue_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Issue
        fields = ('issue_id', 'heading', 'reporter', 'assigned_by', "assigned_to", 'assignedAt', 'updatedAt', 'project',
                  'description', 'tags', 'status')
        read_only_fields = ('assigned_to', 'assignedAt',
                            'assigned_by', 'reporter', 'status', 'updatedAt')
    # def create(self, validated_data):
    #     team = validated_data.pop('team')
    #     project = Project.objects.create(**validated_data)
    #     for member in team:
    #         project.team.add(member)
    #     project.team.add(project.creator)
    #     return project


class IssueUpdateSerializer(serializers.ModelSerializer):
    reporter = serializers.ReadOnlyField(source='reporter.username')
    comment = CommentSerializer(many=True, read_only=True)
    # assigned_by = UserSerializer()
    # assigned_to = UserSerializer()
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='tagname',

    )

    def validate(self, data):
        if (self.context['request'].method == 'PATCH' or self.context['request'].method == 'PUT'):
            if(self.context['request'].user.is_staff or self.context['request'].user.team.filter(id=self.instance.project.id)):

                return data
            if(data.get('assigned_by', None) or data.get('assigned_to', None)):
                raise serializers.ValidationError("Not Allowed")
            return data

        return data

    class Meta:
        model = Issue
        fields = ('project', 'heading', 'reporter', 'comment', 'assigned_by', "assigned_to", 'assignedAt', 'updatedAt',
                  'description', 'tags', 'status')
        read_only_fields = ('heading', 'reporter',
                            'description', 'project', 'updatedAt')
