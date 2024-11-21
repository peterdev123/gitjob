from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate ,login, logout
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm, EditProfileForm, ResumeUploadForm, ProfilePicUploadForm
from .models import GitJobUser, Resume
from .functions import remove_previous_profile_pic, handleResumeUploadForm, handleResumeDeleteForm
import json

# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username_input = form.cleaned_data['username']
            password_input = form.cleaned_data['password']

            user_login = authenticate(username=username_input, password=password_input)

            if user_login is not None:
                login(request, user_login)
                return redirect('/home/')
            else:
                messages.info(request, "Incorrect credentials")
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {"form": form})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            fname_input = form.cleaned_data['fname']
            lname_input = form.cleaned_data['lname']
            email_input = form.cleaned_data['email']
            username_input = form.cleaned_data['username']
            password_input = form.cleaned_data['password']
            retypepassword_input = form.cleaned_data['retypepassword']
            is_business_manager_input = form.cleaned_data['is_business_manager']

            if password_input != retypepassword_input:
                messages.info(request, "Passwords do NOT match")
            else:                
                if GitJobUser.objects.filter(email=email_input).exists():
                    messages.info(request, "Email already used")
                elif GitJobUser.objects.filter(username=username_input).exists():
                    messages.info(request, "Username already used")
                else:
                    user = GitJobUser.objects.create(
                        email=email_input,
                        username=username_input,
                        first_name=fname_input,
                        last_name=lname_input,
                        is_business_manager=is_business_manager_input
                    )
                    user.set_password(password_input)
                    user.save()

                    #auth the user after making account
                    user_login = authenticate(username=username_input, password=password_input)
                    if user_login is not None:
                        login(request, user_login)
                        return redirect('/home/')
                    else:
                        messages.info(request, "Error: Cannot log in registered account...")

    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {"form": form})

def profile_view(request, username):
    #helper method
    def parse_context(user, edit_profile_form, resume_upload_form):
        resumes = Resume.objects.filter(owner=user) or []
        if user.birthdate is not None:
            formatted_birthdate = user.birthdate.strftime("%Y-%m-%d")
        else:
            formatted_birthdate = None
        return {
            "user": user,
            "birthdate": formatted_birthdate,
            "edit_profile_form": edit_profile_form,
            "resume_upload_form": resume_upload_form,
            "resumes": resumes
        }

    if not request.user.is_authenticated:
        return HttpResponse("User not logged in")

    searchedUser = GitJobUser.objects.filter(username=username)

    if not searchedUser.exists():
        messages.info(request, f"User {username} does not exist...")
        return redirect('home')
    
    if username != request.user.username:
        return render(request, "users/profile.html", {'user': searchedUser[0]})

    # if searched user is the current user themselves
    edit_profile_form = EditProfileForm()
    resume_upload_form = ResumeUploadForm()
    profile_pic_upload_form = ProfilePicUploadForm()
    user = request.user

    handleResumeUploadForm(request)
    handleResumeDeleteForm(request)
    if request.method == "POST":
        if request.POST.get('form_type') == 'edit_profile_form':
            edit_profile_form = EditProfileForm(request.POST, instance=user)
            if edit_profile_form.is_valid():
                edit_profile_form.save()
        elif request.POST.get('form_type') == 'profile_pic_upload_form':
            profile_pic_upload_form = ProfilePicUploadForm(request.POST, request.FILES)
            print(request.FILES)
            if profile_pic_upload_form.is_valid():
                profile_picture = request.FILES['profile_picture']
                if str(user.profile_picture) != "users/profile_pictures/default_profile_picture.png":
                    remove_previous_profile_pic(user.profile_picture)
                user.profile_picture = profile_picture
                user.save()
                messages.info(request, "Profile picture successfully updated")
            else:
                print(profile_pic_upload_form.errors)
        elif request.POST.get('form_type') == 'edit_skills_form':
            skills_json_input = request.POST.get('skills_json')
            try:
                skills_list = json.loads(skills_json_input)
            except json.JSONDecodeError:
                skills_list = []
            user.skills = skills_list
            user.save()
        elif request.POST.get('form_type') == 'edit_experiences_form':
            experiences_json_input = request.POST.get('experiences_json')
            try:
                experiences_list = json.loads(experiences_json_input)
            except json.JSONDecodeError:
                experiences_list = []
            user.experiences = experiences_list
            user.save()
        elif request.POST.get('form_type') == 'logout':
            logout(request)
            return redirect('login')
        return redirect('profile', username=user.username)
    
    return render(request, "users/own_profile.html", parse_context(request.user, edit_profile_form, resume_upload_form))