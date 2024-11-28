from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.utils.timezone import now
from datetime import date
from manager.models import JobPost
from .models import JobApplication
from users.models import Resume
from users.forms import ResumeUploadForm
from manager.forms import JobApplicationForm
from users.functions import handleResumeUploadForm, handleResumeDeleteForm
from .functions import get_job_field_color


# Create your views here.
def job_posting_view(request, id):
    job_posting = JobPost.objects.get(id=id)
    # Need to change this on create
    job_posting.tags = job_posting.tags.split(',')

    # Get all job_postings that are not yet done with hiring AND not the current one we are viewing AND ordered by latest datetime added
    other_job_postings = JobPost.objects.filter(hiring_deadline__gte=now().date()).exclude(id=id).order_by('-date_time_added')
    for other_job_posting in other_job_postings:
        other_job_posting.tags = other_job_posting.tags.split(',')
        other_job_posting.color = get_job_field_color(other_job_posting.job_field)
        print(other_job_posting.job_field)
    handleResumeUploadForm(request)
    handleResumeDeleteForm(request)

    # dictionary to check if user already applied, and if true, add the form submitted
    edit_application_fields = {
        'already_applied': False,
    }

    existing_application = None
    if request.user.is_authenticated:
        try:
            existing_application = JobApplication.objects.get(job_post=job_posting, applicant=request.user)
        except JobApplication.DoesNotExist:
            pass

        edit_application_fields['already_applied'] = False
        if existing_application:
            edit_application_fields['already_applied'] = True
            edit_application_fields['form'] = existing_application
        
    if request.method == 'POST': 
        if request.POST.get('form_type') == 'job_application_form':
            job_application_form = JobApplicationForm(request.POST)
            if job_application_form.is_valid():
                resume = get_object_or_404(Resume, id=request.POST.get('resume_id'))
                if request.POST.get('already_applied') == 'True':
                    existing_application.email = request.POST.get('email')
                    existing_application.phone_number = request.POST.get('phone_number')
                    existing_application.cover_letter = request.POST.get('cover_letter')
                    existing_application.resume = resume
                    existing_application.date_updated = date.today()
                    existing_application.save()
                    messages.info(request, "Successfully edited your application entry!")
                else:
                    job_application = job_application_form.save(commit=False)  # Create the instance but don't save yet
                    job_application.job_post = JobPost.objects.get(id=id)
                    job_application.applicant = request.user  # Set the current user as the applicant
                    job_application.resume = resume  # Set the resume
                    job_application.date_updated = date.today()
                    job_application.save()
                    messages.info(request, "Successfully filed a job application form!")
                
            else:
                messages.error(request, "Error: Form submitted is not valid!")

        elif request.POST.get('form_type') == 'cancel_application':
            existing_application.delete()
            messages.info(request, "Successfully cancelled your application to this job posting!")
        
        # redirect the page to reset all input after submitting a form
        return redirect('job_posting', id=id)



    resumes = []
    if request.user.is_authenticated:
        resumes = Resume.objects.filter(owner=request.user)


    return render(request, 'jobs/job_posting.html', {
        'job_posting': job_posting,
        'other_job_postings': other_job_postings,
        'resumes': resumes,
        'resume_upload_form': ResumeUploadForm(),
        'job_application_form': JobApplicationForm(user=request.user, form=existing_application),
        'edit_application_fields': edit_application_fields
        })

def job_post(request):
    job_post = JobPost.objects.filter(author=request.user)
    return render(request, 'jobs/job_post.html', {'job_post' : job_post})

def delete_job_post(request, post_id):
    post = get_object_or_404(JobPost, id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect('job_post') 

def job_application_history_view(request):
    job_applications = request.user.job_applications.all()
    for application in job_applications:
        application.job_post.tags = application.job_post.tags.split(',')
    return render(request, 'jobs/job_application_history.html', {'job_applications': job_applications})
