from django.shortcuts import render

def hero(request):
    
    return render(request, 'gitjob/hero.html')

def homepage(request):

    return render(request, 'gitjob/homepage.html')

def messages(request):

    return render(request, 'gitjob/messages.html')