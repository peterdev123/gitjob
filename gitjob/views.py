from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from manager.models import JobPost
from users.models import GitJobUser

def hero(request):
    
    return render(request, 'gitjob/hero.html')

def homepage(request):
    job_postings = JobPost.objects.all()
    for job_posting in job_postings:
        job_posting.tags = job_posting.tags.split(',')
    return render(request, 'gitjob/homepage.html', {'job_postings': job_postings})

def messages(request):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.POST.get('form_type') == 'search_user':
            keyword = request.POST.get('input_keyword', '')
            users = GitJobUser.objects.filter(
                                    Q(first_name__icontains=keyword) |
                                    Q(last_name__icontains=keyword) |
                                    Q(username__icontains=keyword)
            )
            user_list = [{'username': user.username, 
                          'profile_pic_url': user.profile_picture.url, 
                          'first_name': user.first_name, 
                          "last_name": user.last_name} 
                        for user in users]
            return JsonResponse({'users': user_list})
    return render(request, 'gitjob/messages.html')

def contactus(request):

    return render(request, 'gitjob/contactus.html')

def aboutus(request):

    return render(request, 'gitjob/aboutus.html')