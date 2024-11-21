from django.db import models
from django.conf import settings
from users.models import Resume

class JobPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    job_title = models.CharField(max_length=255)
    job_field = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    hiring_deadline = models.DateField()
    min_salary = models.DecimalField(max_digits=10, decimal_places=2)
    max_salary = models.DecimalField(max_digits=10, decimal_places=2)
    job_description = models.TextField()
    core_competencies = models.TextField()
    
    # Change tags to allow free-form input
    tags = models.TextField(blank=True, help_text="Enter tags separated by commas.")
    
    company_logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return self.job_title

class JobApplication(models.Model):
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.IntegerField(blank=True, null=True)
    cover_letter = models.TextField(max_length=1000)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    date_updated = models.DateField()