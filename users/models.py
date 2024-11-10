from django.contrib.auth.models import AbstractUser
from django.db import models
import os
# class Skill(models.Model):
#     string = models.CharField(max_length=100)

# class Experience(models.Model):
#     string = models.CharField(max_length=100)

class GitJobUser(AbstractUser):
    is_business_manager = models.BooleanField(default=False)
    job = models.CharField(max_length=100, blank=True, null=True)
    job_company = models.CharField(max_length=100, blank=True, null=True)
    home_address = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    skills = models.JSONField(default=list)
    experiences = models.JSONField(default=list)
    profile_picture = models.ImageField(upload_to="users/profile_pictures/", default="users/profile_pictures/default_profile_picture.png")

    def __str__(self):
        return self.username

class Resume(models.Model):
    filename = models.CharField(max_length=100, default="Unnamed Resume.pdf")
    file = models.FileField(upload_to="users/resumes/")
    owner = models.ForeignKey(GitJobUser, on_delete=models.CASCADE)