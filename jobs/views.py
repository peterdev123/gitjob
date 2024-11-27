from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from datetime import date
from manager.models import JobPost
from .models import JobApplication
from users.models import Resume
from users.forms import ResumeUploadForm
from manager.forms import JobApplicationForm
from users.functions import handleResumeUploadForm, handleResumeDeleteForm

# Create your views here.
def job_posting_view(request, id):
    job_posting = JobPost.objects.get(id=id)
    # Need to change this on create
    job_posting.tags = job_posting.tags.split(',')

    other_job_postings = JobPost.objects.all().exclude(id=id)
    for other_job_posting in other_job_postings:
        other_job_posting.tags = other_job_posting.tags.split(',')
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
        
    if request.method == 'POST' and request.POST.get('form_type') == 'job_application_form':
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
            
            # redirect the page to reset all input after submitting a form
            return redirect('job_posting', id=id)
        else:
            messages.error(request, "Error: Form submitted is not valid!")



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
    print(job_post)
    return render(request, 'jobs/job_post.html', {'job_post' : job_post})

def job_application_history_view(request):
    job_applications = request.user.job_applications.all()
    return render(request, 'jobs/job_application_history.html', {'job_applications': job_applications})