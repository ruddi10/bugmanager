from django.db import models
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from projects.models import Issue
from projects.constants import *
from .tagsmodel import Tag
User = get_user_model()


class Comment(models.Model):
    issue = models.ForeignKey(
        Issue, on_delete=models.CASCADE, related_name="comment")
  #  team = models.ManyToManyField(User, blank=True, related_name="team")
    description = RichTextField(blank=True)
    createdAt = models.DateTimeField("Created At", default=timezone.now)
  #  team = models.ManyToManyField(User, blank=True, related_name="team")
    commented_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="your_comments")

    def __str__(self):
        return (f'Comment {self.id} of {self.issue}')

    # @property
    # def assigned(self):
    #     if(self.assigned):
    #         return self.assigned
    #     else:
    #         return "Not Assigned yet"
