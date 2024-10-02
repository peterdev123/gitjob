from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'login_input',
            'placeholder': "Username..."
        })
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'login_input',
            'placeholder': 'Password...'
        })
    )

class RegisterForm(forms.Form):
    fname = forms.CharField(
        label="First Name", 
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'register_input',
            'placeholder': 'First Name...'
        })
    )
    lname = forms.CharField(
        label="Last Name", 
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'register_input',
            'placeholder': 'Last Name...'
        })
    )
    email = forms.EmailField(
        label="Email Address", 
        widget=forms.EmailInput(attrs={
            'class': 'register_input',
            'placeholder': 'Email Address...'
        })
    )
    username = forms.CharField(
        label="Username", 
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'register_input',
            'placeholder': 'Username...'
        })
    )
    password = forms.CharField(
        label="Password", 
        widget=forms.PasswordInput(attrs={
            'class': 'register_input',
            'placeholder': 'Password...'
        })
    )
    retypepassword = forms.CharField(
        label="Retype Password", 
        widget=forms.PasswordInput(attrs={
            'class': 'register_input',
            'placeholder': 'Retype Password...'
        })
    )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label_suffix = ''
