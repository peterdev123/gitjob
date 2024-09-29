from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class GitJobUser(AbstractUser):
    birthdate = models.DateField('birthdate', blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username