from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=255)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="creator")
    team = models.ManyToManyField(User, blank=True, related_name="team")
    wiki = RichTextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", default=timezone.now)

    def __str__(self):
        return self.title
