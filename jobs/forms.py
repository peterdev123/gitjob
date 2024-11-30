from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'cover_letter']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'profile_edit_input',
                'name': 'first_name',
                'placeholder': 'John...', 
                'required': True
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'profile_edit_input',
                'name': 'last_name',
                'placeholder': 'Doe...', 
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'profile_edit_input',
                'name': 'email',
                'placeholder': 'john@email.co...', 
                'required': True
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'profile_edit_input',
                'name': 'phone_number',
                'placeholder': '0912345...', 
                'required': True
            }),
            'cover_letter': forms.Textarea(attrs={
                'class': 'w-full h-48 mt-4 rounded-2xl border-2 border-gray-300',
                'name': 'cover_letter',
                'placeholder': 'I think I am fit for this job because...',
                'required': True
            })
        }
    def __init__(self, *args, user=None, form=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            # make the fields readonly
            self.fields['first_name'].widget.attrs['readonly'] = True
            self.fields['last_name'].widget.attrs['readonly'] = True

            if user.is_authenticated:
                self.fields['first_name'].initial = user.first_name
                self.fields['last_name'].initial = user.last_name
                self.fields['email'].initial = user.email
                self.fields['phone_number'].initial = user.phone_number
            
            if form:
                self.fields['email'].initial = form.email
                self.fields['phone_number'].initial = form.phone_number
                self.fields['cover_letter'].initial = form.cover_letter