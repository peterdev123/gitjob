from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth import get_user_model
from .forms import LoginForm, RegisterForm

# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            return render(request, 'jobs/home.html', {'username': username})
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {"form": form})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            fnameInput = form.cleaned_data['fname']
            lnameInput = form.cleaned_data['lname']
            emailInput = form.cleaned_data['email']
            usernameInput = form.cleaned_data['username']
            passwordInput = form.cleaned_data['password']
            retypepasswordInput = form.cleaned_data['retypepassword']

            if passwordInput != retypepasswordInput:
                messages.info(request, "Passwords do NOT match")
            else:
                User = get_user_model()
                if User.objects.filter(username=usernameInput).exists():
                    messages.info(request, "Username already used")
                elif User.objects.filter(email=emailInput).exists():
                    messages.info(request, "Email already used")
                else:
                    user = User.objects.create_user(
                        email=emailInput,
                        username=usernameInput,
                        password=passwordInput
                    )
                    user.first_name = fnameInput
                    user.last_name = lnameInput
                    user.save()
                    return render(request, 'jobs/home.html')            

    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {"form": form})