from django.db import models
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone

User = get_user_model()


class Project(models.Model):
    title = models.CharField(max_length=255)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="creator")
    team = models.ManyToManyField(User, blank=True, related_name="team")
    wiki = RichTextField(blank=True)
    createdAt = models.DateTimeField("Created At", default=timezone.now)
    is_deployed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # @property
    # def issues(self):
    #     return self.bugs
    def team_list(self):
        return (list(map(lambda x: {'id': x.id, 'username': x.username, 'profilepic': x.profile.profilepic}, self.team.all())))

    def get_creator(self):
        return {"id": self.creator.id, "name": self.creator.username, }

    def total_bugs(self):
        return self.bugs.all().count()
