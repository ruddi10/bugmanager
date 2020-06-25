from django.db import models
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from projects.models import Project
from projects.constants import *
from .tagsmodel import Tag
User = get_user_model()


class Issue(models.Model):
    heading = models.CharField(max_length=255)
    reporter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reporter")
  #  team = models.ManyToManyField(User, blank=True, related_name="team")
    description = RichTextField(blank=True)
    createdAt = models.DateTimeField("Created At", default=timezone.now)
    tags = models.ManyToManyField(Tag, related_name="issues")
    status = models.CharField(
        max_length=30, choices=StatusCode.choices, default=StatusCode.PENDING)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="bugs")

    assigned_to = models.ForeignKey(
        User, models.SET_NULL,
        blank=True,
        null=True,
        related_name="assigned_issues")
  #  team = models.ManyToManyField(User, blank=True, related_name="team")
    assigned_by = models.ForeignKey(
        User, models.SET_NULL,
        blank=True,
        null=True,
        related_name="issues_you_assigned")
    assignedAt = models.DateTimeField(
        "Assigned At", blank=True, null=True, default=timezone.now)
    createdAt = models.DateTimeField(
        "Updated At", blank=True, null=True, auto_now_add=True)
    updatedAt = models.DateTimeField(
        "Updated At", blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.heading

    # @property
    # def comments(self):
    #     if(self.comment):
    #         return self.comment
    #     else:
    #         return "Not Assigned yet"
