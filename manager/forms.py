from django import forms
from .models import JobPost, JobApplication

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['job_title', 'job_field', 'job_schedule', 'address', 'hiring_deadline', 
                  'min_salary', 'max_salary', 'job_description', 
                  'core_competencies', 'tags', 'company_logo']
        
        widgets = {
            'job_title': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-3 bg-gray-50 focus:ring-2 focus:ring-blue-500 focus:outline-none', 
                'placeholder': 'Enter Job Title', 
                'required': True
            }),
            'job_field': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-3 bg-gray-50 focus:ring-2 focus:ring-blue-500 focus:outline-none', 
                'placeholder': 'Enter Job Field', 
                'required': True
            }),
            'job_schedule': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-3 bg-gray-50 focus:ring-2 focus:ring-blue-500 focus:outline-none', 
                'placeholder': 'Select Job Schedule', 
                'required': True
            }),
            'address': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-3 bg-gray-50 focus:ring-2 focus:ring-blue-500 focus:outline-none', 
                'placeholder': 'Enter Company Address', 
                'required': True
            }),
            'hiring_deadline': forms.DateInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-3 bg-gray-50 focus:ring-2 focus:ring-blue-500 focus:outline-none', 
                'type': 'date', 
                'required': True
            }),
            'min_salary': forms.NumberInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-3 bg-gray-50 focus:ring-2 focus:ring-blue-500 focus:outline-none', 
                'placeholder': 'Enter Minimum Salary', 
                'required': True
            }),
            'max_salary': forms.NumberInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-3 bg-gray-50 focus:ring-2 focus:ring-blue-500 focus:outline-none', 
                'placeholder': 'Enter Maximum Salary', 
                'required': True
            }),
            'job_description': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-3 bg-gray-50 focus:ring-2 focus:ring-blue-500 focus:outline-none', 
                'rows': 4, 
                'placeholder': 'Enter Job Description', 
                'required': True
            }),
            'core_competencies': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-3 bg-gray-50 focus:ring-2 focus:ring-blue-500 focus:outline-none', 
                'rows': 3, 
                'placeholder': 'Enter Core Competencies', 
                'required': True
            }),
            'tags': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-3 bg-gray-50 focus:ring-2 focus:ring-blue-500 focus:outline-none', 
                'placeholder': 'Enter Tags (comma-separated)', 
                'required': True
            }),
            'company_logo': forms.FileInput(attrs={
                'class': 'block w-full text-gray-700 font-medium cursor-pointer bg-gray-50 rounded-lg p-3 focus:ring-2 focus:ring-blue-500 focus:outline-none', 
                'required': True
            }),
        }

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
                'class': 'w-full h-32 mt-4 rounded-2xl border-2 border-gray-300',
                'name': 'cover_letter',
                'placeholder': 'I think I am fit for this job because...',
                'required': True
            })
        }
    def __init__(self, *args, user=None, form=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            # Set initial values and make the fields readonly
            self.fields['first_name'].initial = user.first_name
            self.fields['first_name'].widget.attrs['readonly'] = True

            self.fields['last_name'].initial = user.last_name
            self.fields['last_name'].widget.attrs['readonly'] = True

            self.fields['email'].initial = user.email
            self.fields['phone_number'].initial = user.phone_number
            
            if form:
                self.fields['email'].initial = form.email
                self.fields['phone_number'].initial = form.phone_number
                self.fields['cover_letter'].initial = form.cover_letter


