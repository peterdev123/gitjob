from django.db import models
from django.conf import settings
from users.models import Resume

class JobPost(models.Model):

    JOB_FIELD_CHOICES = [
        ('architecture_engineering', 'Architecture and Engineering'),
        ('arts_entertainment', 'Arts and Entertainment'),
        ('business_management', 'Business Management and Administration'),
        ('communications', 'Communications'),
        ('education', 'Education'),
        ('it', 'IT'),
        ('repair_maintenance', 'Repair and Maintenance'),
        ('agriculture', 'Agriculture'),
        ('health_medicine', 'Health and Medicine'),
        ('law_public_policy', 'Law and Public policy'),
        ('sales', 'Sales'),
        ('others', 'Others'),
    ]

    JOB_SCHED_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('internship', 'Internship'),
        ('project_work', 'Project Work'),
        ('select', 'Select'),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    job_title = models.CharField(max_length=255)
    job_field = models.CharField(max_length=255,choices=JOB_FIELD_CHOICES,default='others')
    job_schedule = models.CharField(max_length=255,choices=JOB_SCHED_CHOICES,default='select')
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