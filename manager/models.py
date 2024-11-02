from django.db import models

class JobPost(models.Model):
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
