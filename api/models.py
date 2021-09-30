import uuid
from django.db import models


class UserSession(models.Model):
    session_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=80, blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    data = models.JSONField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.category}'