from django.shortcuts import render, redirect
from .forms import JobPostForm

def post_jobs(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/home/')  # Redirect to a success page after submission
    else:
        form = JobPostForm()

    return render(request, 'manager/post_jobs.html', {'form': form})
