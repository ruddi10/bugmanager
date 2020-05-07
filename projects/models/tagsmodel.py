from django.db import models
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone

User = get_user_model()


class Tag(models.Model):
    tagname = models.CharField(max_length=255)

    def __str__(self):
        return self.tagname

    # @property
    # def issues(self):
    #     return self.bugs
