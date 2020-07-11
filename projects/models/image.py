from django.db import models
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from projects.models import Project
from projects.constants import *
from .tagsmodel import Tag


User = get_user_model()


class Image(models.Model):
    image = models.ImageField(upload_to="uploads")
