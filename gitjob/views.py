from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Q
from manager.models import JobPost
from users.models import GitJobUser
from django.contrib.auth.decorators import login_required
from .models import ChatGroup, GroupMessage
from .forms import ChatmessageCreateForm

def hero(request):
    
    return render(request, 'gitjob/hero.html')

def homepage(request):
    job_postings = JobPost.objects.all()
    for job_posting in job_postings:
        job_posting.tags = job_posting.tags.split(',')
    return render(request, 'gitjob/homepage.html', {'job_postings': job_postings})

@login_required
def messages(request):
    # if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
    #     if request.POST.get('form_type') == 'search_user':
    #         keyword = request.POST.get('input_keyword', '')
    #         users = GitJobUser.objects.filter(
    #                                 Q(first_name__icontains=keyword) |
    #                                 Q(last_name__icontains=keyword) |
    #                                 Q(username__icontains=keyword)
    #         )
    #         user_list = [{'username': user.username, 
    #                       'profile_pic_url': user.profile_picture.url, 
    #                       'first_name': user.first_name, 
    #                       "last_name": user.last_name} 
    #                     for user in users]
    #         return JsonResponse({'users': user_list})
    chat_group = get_object_or_404(ChatGroup, group_name="public-chat")
    chat_messages = chat_group.chat_messages.all()[:30]
    form = ChatmessageCreateForm()

    # Handle HTMX form submission
    if request.htmx:
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            context = {'message': message}
            return render(request, 'gitjob/partials/chat_message_p.html', context)

    # Normal GET request (initial page load)
    return render(request, 'gitjob/messages.html', {'chat_messages': chat_messages, 'form': form})

def contactus(request):

    return render(request, 'gitjob/contactus.html')

def aboutus(request):

    return render(request, 'gitjob/aboutus.html')