from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusCode(models.TextChoices):
    PENDING = 'P', _('Pending')
    TBD = 'TBD', _('To-Be-Disscussed')
    RESOLVED = 'R', _('Resolved')

