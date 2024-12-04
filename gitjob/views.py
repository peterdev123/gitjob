from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Q, Max
from django.utils.timezone import now
from manager.models import JobPost
from users.models import GitJobUser
from jobs.models import JobApplication
from django.conf import settings 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import Http404
from .models import ChatGroup
from .forms import ChatmessageCreateForm
from jobs.functions import get_job_field_color
from django.db.models import Subquery
from .models import GroupMessage
from .models import Notification
from django.urls import reverse


def hero(request):
    return render(request, 'gitjob/hero.html')

def homepage(request):
    if not request.user.is_authenticated:
        return render(request, 'gitjob/homepage.html')

    applied_job_ids = JobApplication.objects.filter(applicant=request.user).values('job_post')

    # get all JobPosts that still hiring
    # AND exclude job_posts that are added by the current user (they will not see their own post)
    # sorted by latest datetime added
    job_postings = JobPost.objects.filter(hiring_deadline__gte=now().date())\
        .exclude(author=request.user)\
        .exclude(id__in=Subquery(applied_job_ids))\
        .order_by('-date_time_added')
    for job_posting in job_postings:
        job_posting.tags = job_posting.tags.split(',')
        job_posting.tags = filter(None, job_posting.tags)
        job_posting.color = get_job_field_color(job_posting.job_field)
    return render(request, 'gitjob/homepage.html', {'job_postings': job_postings})

@login_required
def messages(request, chatroom_name='public-chat'):
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
        
    # For default chat groups if empty
    if not ChatGroup.objects.filter(group_name="public-chat").exists():
        public_group = ChatGroup.objects.create(
            group_name = "public-chat",
            is_private = False
        )

        user = get_user_model().objects.get(id=1)
        public_group.members.add(user)

    # For private chat groups
    chat_group = get_object_or_404(ChatGroup, group_name=chatroom_name)
    chat_messages = chat_group.chat_messages.all()[:30]

    chat_groups = ChatGroup.objects.filter(members=request.user).annotate(
        latest_message_date=Max('chat_messages__created')
    ).order_by('-latest_message_date')
    
    filtered_chat_groups = []
    for group in chat_groups:
        messages_between_users = group.chat_messages.filter(
            author=request.user
        ) | group.chat_messages.filter(
            author__in=group.members.exclude(id=request.user.id)
        )

        if messages_between_users.exists():
            filtered_chat_groups.append(group)

            latest_message = messages_between_users.order_by('-created').first()
            group.latest_message_body = latest_message.body if latest_message else "No messages yet"
        else:
            group.latest_message_body = "No messages yet"

    # For chats
    form = ChatmessageCreateForm()

    other_user = None
    if chat_group.is_private:
        if request.user not in chat_group.members.all():
            raise Http404()
        for member in chat_group.members.all():
            if member != request.user:
                other_user = member
                break

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
    
    context = {
        'chat_messages' : chat_messages,
        'form' : form,
        'other_user' : other_user,
        'chatroom_name' : chatroom_name,
        'chat_groups' : filtered_chat_groups,
    }

    # Normal GET request (initial page load)
    return render(request, 'gitjob/messages.html', context)

def get_or_create_chatroom(request, username):
    if request.user.username == username:
        return redirect('home')
    
    User = get_user_model()
    other_user = User.objects.get(username=username)
    
    # Check if there is an existing private chat room with this user
    my_private_chatrooms = request.user.chat_groups.filter(is_private=True)
    if my_private_chatrooms.exists():
        for chatroom in my_private_chatrooms:
            if other_user in chatroom.members.all():
                return redirect('chatroom', chatroom.group_name)
   
    # Create a new private chat room if one doesn’t exist
    chatroom = ChatGroup.objects.create(is_private=True)
    chatroom.members.add(other_user, request.user)
    
    return redirect('chatroom', chatroom.group_name)

@login_required
def fetch_notifications(request):
    if request.method == "GET" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Fetch chat-related notifications
        latest_messages = (
            GroupMessage.objects.filter(group__members=request.user)
            .exclude(author=request.user)
            .values('author')
            .annotate(latest_message_id=Max('id'))
        )
        latest_message_ids = [entry['latest_message_id'] for entry in latest_messages]
        chat_notifications = (
            GroupMessage.objects.filter(id__in=latest_message_ids)
            .select_related('author', 'group')
            .order_by('-created')
        )

        # Fetch job application acceptance notifications
        acceptance_notifications = Notification.objects.filter(
            recipient=request.user,
            is_read=False  
        ).order_by('-created_at')

        # Combine both types of notifications
        notifications_data = []

        # Add chat notifications
        for message in chat_notifications:
            notifications_data.append({
                "imageUrl": message.author.profile_picture.url if message.author.profile_picture else "/static/default_profile_pic.jpg",
                "author": message.author.username,
                "message": f"<strong>{message.author.username}</strong> from <strong>{message.author.job_company}</strong> has sent you a message."
                if message.author.job_company else f"<strong>{message.author.username}</strong> has sent you a message.",
                "url": "/messages/",
                "created": message.created.strftime("%Y-%m-%d %H:%M:%S"),
            })

        # Add job acceptance notifications
        for notification in acceptance_notifications:
            notifications_data.append({
                "imageUrl": notification.image_url,
                "author": "System",
                "message": notification.message,
                "url": reverse('job_application_history'),
                "created": notification.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            })

        notifications_data.sort(key=lambda x: x["created"], reverse=True)
        return JsonResponse({"notifications": notifications_data})

    return JsonResponse({"notifications": []})


def contactus(request):

    return render(request, 'gitjob/contactus.html')

def aboutus(request):

    return render(request, 'gitjob/aboutus.html')