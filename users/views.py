from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate ,login
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from .forms import LoginForm, RegisterForm, EditProfileForm
from .models import GitJobUser
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

def profile_view(request):
    if request.user.is_authenticated:
        user = request.user

        if user.skills:
            skills_json = json.dumps(user.skills)
        else:
            skills_json = json.dumps([])
        if user.experiences:
            experiences_json = json.dumps(user.experiences)
        else:
            experiences_json = json.dumps([])

        if request.method == "POST":
            if request.POST.get('form_type') == 'edit_profile_form':
                form = EditProfileForm(request.POST, instance=user)
                if form.is_valid():
                    form.save()
                    return redirect('profile')
            elif request.POST.get('form_type') == 'edit_skills_form':
                skills_json_input = request.POST.get('skills_json')
                try:
                    skills_list = json.loads(skills_json_input)
                except json.JSONDecodeError:
                    skills_list = []
                user.skills = skills_list
                user.save()
                form = EditProfileForm()
                skills_json = json.dumps(user.skills)
                return render(request, "users/profile.html", {"user": request.user, "form": form, "skills_json": skills_json, "experiences_json": experiences_json})
            elif request.POST.get('form_type') == 'edit_experiences_form':
                experiences_json_input = request.POST.get('experiences_json')
                try:
                    experiences_list = json.loads(experiences_json_input)
                except json.JSONDecodeError:
                    experiences_list = []
                user.experiences = experiences_list
                user.save()
                form = EditProfileForm()
                experiences_json = json.dumps(user.experiences)
                return render(request, "users/profile.html", {"user": request.user, "form": form, "skills_json": skills_json, "experiences_json": experiences_json})
        else:
            form = EditProfileForm()
            return render(request, "users/profile.html", {"user": request.user, "form": form, "skills_json": skills_json, "experiences_json": experiences_json})
    else:
        return HttpResponse("User not logged in")