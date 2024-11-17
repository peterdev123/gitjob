from django.shortcuts import render 
from manager.models import JobPost

# Create your views here.
def job_posting_view(request, id):
    job_posting = JobPost.objects.get(id=id)
    # Need to change this on create
    job_posting.tags = job_posting.tags.split(',')

    other_job_postings = JobPost.objects.all().exclude(id=id)
    for other_job_posting in other_job_postings:
        other_job_posting.tags = other_job_posting.tags.split(',')
    return render(request, 'jobs/job_posting.html', {'job_posting': job_posting, 'other_job_postings': other_job_postings})

def job_post(request):
    job_post = JobPost.objects.filter(author=request.user)
    print(job_post)
    return render(request, 'jobs/job_post.html', {'job_post' : job_post})