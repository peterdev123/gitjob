from django import forms
from .models import GitJobUser, Resume

class LoginForm(forms.Form):
    def input_attrs(placeholder):
        return {
            'class': 'login_input',
            'placeholder': placeholder
        }
    
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
    def input_attrs(placeholder):
        return {
            'class': 'register_input',
            'placeholder': placeholder
        }
    fname = forms.CharField(
        label='', 
        max_length=50,
        widget=forms.TextInput({
            'class': 'register_input name_input',
            'placeholder': 'First Name...'
        })
    )
    lname = forms.CharField(
        label="", 
        max_length=50,
        widget=forms.TextInput({
            'class': 'register_input name_input',
            'placeholder': 'Last Name...'
        })
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
    is_business_manager = forms.BooleanField(
        label="Register as Business Manager", required=False
    )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            if not isinstance(field, forms.BooleanField):
                field.label = ""

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = GitJobUser
        fields = ['username', 'job', 'job_company', 'home_address', 'country' , 'phone_number', 'birthdate', 'gender', 'description']
    
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], required=False)

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None

class ResumeUploadForm(forms.Form):
    resume_file = forms.FileField(widget=forms.FileInput(attrs={
        'accept': 'application/pdf',
        'class': 'resume_input'
        }))

class ProfilePicUploadForm(forms.Form):
    profile_pic = forms.ImageField(required=False)