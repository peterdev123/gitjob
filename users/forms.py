from django import forms
from .models import GitJobUser

def input_attrs(placeholder):
    return {
        'class': 'login_register_input',
        'placeholder': placeholder
    }

class LoginForm(forms.Form):
    username = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs=input_attrs("Username..."))
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs=input_attrs("Password..."))
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ""

class RegisterForm(forms.Form):
    fname = forms.CharField(
        label='', 
        max_length=50,
        widget=forms.TextInput(attrs=input_attrs("First Name..."))
    )
    lname = forms.CharField(
        label="", 
        max_length=50,
        widget=forms.TextInput(attrs=input_attrs("Last Name..."))
    )
    email = forms.EmailField(
        label="Email Address", 
        widget=forms.EmailInput(attrs=input_attrs("Email Address.."))
    )
    username = forms.CharField(
        label="Username", 
        max_length=30,
        widget=forms.TextInput(attrs=input_attrs("Username..."))
    )
    password = forms.CharField(
        label="Password", 
        widget=forms.PasswordInput(attrs=input_attrs("Password..."))
    )
    retypepassword = forms.CharField(
        label="Retype Password", 
        widget=forms.PasswordInput(attrs=input_attrs("Retype Password..."))
    )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ""

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = GitJobUser
        fields = ['username', 'job', 'job_company', 'home_address', 'phone_number', 'birthdate', 'gender', 'description']
    
    birthdate = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], required=False)
    # description = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None