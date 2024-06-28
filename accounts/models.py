 #  code for accounts

# Create your models here.
# accounts/models.py
from django.db import models
import uuid

class Account(models.Model):
    account_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
 #user account id
    email = models.EmailField(unique=True)
 #email should be unique
    account_name = models.CharField(max_length=255)
 #account name can be anything
    app_secret_token = models.CharField(max_length=255, unique=True, editable=False)
    website = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.app_secret_token:
            self.app_secret_token = uuid.uuid4().hex
        super().save(*args, **kwargs)

    def __str__(self):
        return self.account_name
