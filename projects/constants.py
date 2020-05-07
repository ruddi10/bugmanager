from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusCode(models.TextChoices):
    PENDING = 'P', _('Pending')
    TBD = 'TBD', _('To-Be-Disscussed')
    RESOLVED = 'R', _('Resolved')


class Tag(models.TextChoices):
    ENHANCE = 'ENH', _('Enchancement')
    UIUX = 'U', _('UI/UX')
    BUG = 'BUG', _('Bug')
    BCP = 'BCP', _('Browser Compatibility Problem')
    SECURITY = "SEC", _('Security')
    CRASH = 'C', _('Crash')

    #GRADUATE = 'GR', _('Graduate')
