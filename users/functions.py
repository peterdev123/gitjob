import os
from django.contrib import messages
from users.forms import ResumeUploadForm
from users.models import Resume

def remove_previous_profile_pic(file):
    os.remove(file.path)

def handleResumeUploadForm(request):
    if request.method == 'POST' and request.POST.get('form_type') == 'resume_upload_form':
            resume_upload_form = ResumeUploadForm(request.POST, request.FILES)
            if resume_upload_form.is_valid():
                resume_file = request.FILES['resume_file']
                resume = Resume.objects.create(
                    filename=str(resume_file),
                    file=resume_file,
                    owner=request.user
                )
                resume.save()
                messages.info(request, f"Resume {str(resume_file)} uploaded successfully")

