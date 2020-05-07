from django.db import models
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from projects.models import Project
from multiselectfield import MultiSelectField
from projects.constants import *
User = get_user_model()


class Issue(models.Model):
    heading = models.CharField(max_length=255)
    reporter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reporter")
  #  team = models.ManyToManyField(User, blank=True, related_name="team")
    description = RichTextField(blank=True)
    createdAt = models.DateTimeField("Created At", default=timezone.now)
    tags = MultiSelectField(
        choices=Tag.choices, max_choices=3, max_length=3)
    status = models.CharField(
        max_length=3, choices=StatusCode.choices, default=StatusCode.PENDING)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="bugs")

    def __str__(self):
        return self.heading

    @property
    def assigned(self):
        if(self.assigned):
            return self.assigned
        else:
            return "Not Assigned yet"
