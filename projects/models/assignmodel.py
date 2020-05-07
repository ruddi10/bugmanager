# from django.db import models
# from django.contrib.auth import get_user_model
# #from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
# from django.utils import timezone
# from projects.models import Issue
# from multiselectfield import MultiSelectField
# from projects.constants import *
# User = get_user_model()


# class IssueAssign(models.Model):
#     issue = models.OneToOneField(
#         Issue, on_delete=models.CASCADE, related_name="assigned")
#     assigned_to = models.ForeignKey(
#         User, models.SET_NULL,
#         blank=True,
#         null=True,
#         related_name="assigned_issues")
#   #  team = models.ManyToManyField(User, blank=True, related_name="team")
#     assigned_by = models.ForeignKey(
#         User, models.SET_NULL,
#         blank=True,
#         null=True,
#         related_name="issues_you_assigned")
#     assignedAt = models.DateTimeField("Assigned At", default=timezone.now)

#     def __str__(self):
#         return self.issue.heading
