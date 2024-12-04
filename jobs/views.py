from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.utils.timezone import now
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.db.models import Subquery
from .models import JobApplication
from .forms import JobApplicationForm
from .functions import get_job_field_color
from manager.models import JobPost
from users.models import Resume
from users.forms import ResumeUploadForm
from users.functions import handleResumeUploadForm, handleResumeDeleteForm
from datetime import date
from gitjob.models import Notification

@csrf_exempt
def update_application_status(request):
    if request.method == 'POST':
        app_id = request.POST.get('app_id')
        new_status = request.POST.get('status')
        try:
            with transaction.atomic():
                # Fetch the JobApplication object
                application = get_object_or_404(JobApplication, id=app_id)
                # Update the status
                application.status = int(new_status)  # Assuming 1 = Accepted, 2 = Declined
                application.save()
                # Create a notification if the application is accepted
                if int(new_status) == 1:  # Assuming 1 = Accepted
                    Notification.objects.create(
                        recipient=application.applicant,  
                        message=f"Your application for <strong>{application.job_post.job_title}</strong> has been accepted!",
                        image_url="/static/images/job-accepted.png"
                    )
                if int(new_status) == 2:
                    Notification.objects.create(
                        recipient=application.applicant,  
                        message=f"Your application for <strong>{application.job_post.job_title}</strong> has been rejected.",
                        image_url="/static/images/job-rejected.png"
                    )
            return JsonResponse({'success': True, 'status': application.status})
        except JobApplication.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Application not found'})
    
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)


# Create your views here.
def job_posting_view(request, id):
    job_posting = JobPost.objects.get(id=id)
    # Need to change this on create
    job_posting.tags = job_posting.tags.split(',')

    applied_job_ids = JobApplication.objects.filter(applicant=request.user).values('job_post')

    # Get all job_postings that are not yet done with hiring 
    # AND not the current one we are viewing 
    # AND not authored but the current user
    # AND not yet applied jobs
    # AND ordered by latest datetime added
    other_job_postings = JobPost.objects.filter(hiring_deadline__gte=now().date())\
        .exclude(id=id)\
        .exclude(author=request.user)\
        .exclude(id__in=Subquery(applied_job_ids))\
        .order_by('-date_time_added')
    
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
                    existing_application.phone_number = request.POST.get('phone_number')
                    existing_application.cover_letter = request.POST.get('cover_letter')
                    existing_application.resume = resume
                    existing_application.datetime_updated = now()
                    existing_application.save()
                    messages.info(request, "Successfully edited your application entry!")
                else:
                    job_application = job_application_form.save(commit=False)  # Create the instance but don't save yet
                    job_application.job_post = JobPost.objects.get(id=id)
                    job_application.applicant = request.user  # Set the current user as the applicant
                    job_application.resume = resume  # Set the resume
                    job_application.datetime_updated = now()
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
    job_post = get_object_or_404(JobPost, id=post_id)
    job_post.delete()
    return redirect('job_post')
 

def job_application_history_view(request):
    job_applications = request.user.job_applications.all().order_by('-datetime_updated')
    for application in job_applications:
        application.job_post.tags = application.job_post.tags.split(',')
    return render(request, 'jobs/job_application_history.html', {'job_applications': job_applications})
