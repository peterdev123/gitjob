from django.shortcuts import render
from manager.models import JobPost

def hero(request):
    
    return render(request, 'gitjob/hero.html')

def homepage(request):
    job_postings = JobPost.objects.all()
    for job_posting in job_postings:
        job_posting.tags = job_posting.tags.split(',')
    return render(request, 'gitjob/homepage.html', {'job_postings': job_postings})

def messages(request):

    return render(request, 'gitjob/messages.html')