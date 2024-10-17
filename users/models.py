from django.contrib.auth.models import AbstractUser
from django.db import models
# class Skill(models.Model):
#     string = models.CharField(max_length=100)

# class Experience(models.Model):
#     string = models.CharField(max_length=100)

class GitJobUser(AbstractUser):
    job = models.CharField(max_length=100, blank=True, null=True)
    job_company = models.CharField(max_length=100, blank=True, null=True)
    home_address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    # skills = models.ManyToManyField(Skill)
    # experiences = models.ManyToManyField(Experience)
    skills = models.JSONField(default=list)
    experiences = models.JSONField(default=list)

    def __str__(self):
        return self.username

class Resume(models.Model):
    file = models.FileField(upload_to="pdf")
    owner = models.ForeignKey(GitJobUser, on_delete=models.CASCADE)