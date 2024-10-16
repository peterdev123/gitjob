from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate ,login
from .forms import LoginForm, RegisterForm

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
                User = get_user_model()
                if User.objects.filter(email=email_input).exists():
                    messages.info(request, "Email already used")
                elif User.objects.filter(username=username_input).exists():
                    messages.info(request, "Username already used")
                else:
                    user = User.objects.create_user(
                        email=email_input,
                        username=username_input,
                        password=password_input,
                        first_name=fname_input,
                        last_name=lname_input,
                    )
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