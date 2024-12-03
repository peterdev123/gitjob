from django.db import models
from django.conf import settings
from manager.models import JobPost
from users.models import Resume
from django.utils import timezone

STATUS_CHOICES = [
    (0, 'Pending'),
    (1, 'Accepted'),
    (2, 'Declined'),
]

# Create your models here.
class JobApplication(models.Model):
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='job_applications')
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='job_applications')
    email = models.EmailField()
    phone_number = models.IntegerField(blank=True, null=True)
    cover_letter = models.TextField(max_length=1000)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    date_updated = models.DateField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0) # 0 - undecided, 1 - accepted, 2 - declined



