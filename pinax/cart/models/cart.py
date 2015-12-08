from django.conf import settings
from django.db import models


class Cart(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
