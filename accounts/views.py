from django.shortcuts import render
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
    return render(request, 'accounts/login.html', {"form": form})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            email = form.cleaned_data['fname']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            retypepassword = form.cleaned_data['retypepassword']
            return render(request, 'jobs/home.html', {'username': username})
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {"form": form})

