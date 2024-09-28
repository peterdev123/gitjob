from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    fname = forms.CharField(label="First Name", max_length=100)
    lname = forms.CharField(label="Last Name", max_length=100)
    email = forms.EmailField(label="Email Address")
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    retypepassword = forms.CharField(label="Password", widget=forms.PasswordInput)
