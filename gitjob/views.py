from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Q
from manager.models import JobPost
from users.models import GitJobUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import Http404
from .models import ChatGroup
from .forms import ChatmessageCreateForm



def hero(request):
    
    return render(request, 'gitjob/hero.html')

def homepage(request):
    job_postings = JobPost.objects.all()
    for job_posting in job_postings:
        job_posting.tags = job_posting.tags.split(',')
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
    # For private chat groups
    chat_group = get_object_or_404(ChatGroup, group_name=chatroom_name)
    chat_messages = chat_group.chat_messages.all()[:30]

    chat_groups = ChatGroup.objects.filter(members=request.user)
    filtered_chat_groups = []

    for group in chat_groups:
        # Check if there are messages in the group where the user has participated
        if group.chat_messages.filter(author=request.user).exists():
            filtered_chat_groups.append(group)
            # Get the latest message for preview
            latest_message = group.chat_messages.order_by('-created').first()
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

def contactus(request):

    return render(request, 'gitjob/contactus.html')

def aboutus(request):

    return render(request, 'gitjob/aboutus.html')