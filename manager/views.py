from django.shortcuts import get_object_or_404, render, redirect
from manager.models import JobPost
from .forms import JobPostForm
from datetime import datetime

def post_jobs(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('/home/')  
    else:
        form = JobPostForm()

    return render(request, 'manager/post_jobs.html', {'form': form})

def edit_job_post(request, post_id):
    post = get_object_or_404(JobPost, id=post_id)
    if request.method == "POST":
        form = JobPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form = JobPostForm(instance=post)
    return render(request, 'manager/edit_post_jobs.html', {'form': form})