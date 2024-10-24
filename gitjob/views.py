from django.shortcuts import render

def hero(request):
    
    return render(request, 'gitjob/hero.html')

def homepage(request):

    return render(request, 'gitjob/homepage.html')

def messages(request):

    return render(request, 'gitjob/messages.html')

def post_jobs(request):

    return render(request, 'gitjob/post_jobs.html')