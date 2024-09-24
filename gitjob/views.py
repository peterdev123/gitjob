from django.shortcuts import render

def hero(request):
    
    return render(request, 'gitjob/hero.html')