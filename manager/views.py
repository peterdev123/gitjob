from django.shortcuts import render, redirect
from .forms import JobPostForm
from datetime import datetime

def post_jobs(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('/home/')  # Redirect to a success page after submission
    else:
        form = JobPostForm()

    return render(request, 'manager/post_jobs.html', {'form': form})
