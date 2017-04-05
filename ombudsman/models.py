import uuid

from django.db import models
from django.contrib.auth.models import User

class ApiKeyGrant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    app_url = models.URLField(verbose_name="App URL", max_length=1024)

    created = models.DateField(auto_now_add=True, null=True)
    updated = models.DateField(auto_now=True, null=True)

    api_key = models.UUIDField(default=uuid.uuid4)
