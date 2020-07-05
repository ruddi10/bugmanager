from django.db import models
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from projects.models import Project
from projects.constants import *
from .tagsmodel import Tag
User = get_user_model()


class Profile(models.Model):
    User = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    enrolment_number = models.CharField(max_length=15, unique=True)
    access_token = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_disabled = models.BooleanField(default=False)
    # profilepic = models.ImageField(
    #     default="guest-user.jpg", null=True, blank=True)
    profilepic = models.TextField(
        default="http://localhost:8000/images/guest-user.jpg")

    def __str__(self):
        return self.enrolment_number
