from django import forms
from .models import JobPost

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['job_title', 'job_field', 'address', 'hiring_deadline', 
                  'min_salary', 'max_salary', 'job_description', 
                  'core_competencies', 'tags', 'company_logo']
        
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'w-full border border-black rounded-lg p-2', 'placeholder': 'Enter Job Title', 'required': True}),
            'job_field': forms.TextInput(attrs={'class': 'w-full border border-black rounded-lg p-2', 'placeholder': 'Enter Job Field', 'required': True}),
            'address': forms.TextInput(attrs={'class': 'w-full border border-black rounded-lg p-2', 'placeholder': 'Enter Company Address', 'required': True}),
            'hiring_deadline': forms.DateInput(attrs={'class': 'w-full border border-black rounded-lg p-2', 'type': 'date', 'required': True}),
            'min_salary': forms.NumberInput(attrs={'class': 'w-full border border-black rounded-lg p-2', 'placeholder': 'Enter Minimum Salary', 'required': True}),
            'max_salary': forms.NumberInput(attrs={'class': 'w-full border border-black rounded-lg p-2', 'placeholder': 'Enter Maximum Salary', 'required': True}),
            'job_description': forms.Textarea(attrs={'class': 'w-full border border-black rounded-lg p-2', 'rows': 4, 'placeholder': 'Enter Job Description', 'required': True}),
            'core_competencies': forms.Textarea(attrs={'class': 'w-full border border-black rounded-lg p-2', 'rows': 3, 'placeholder': 'Enter Core Competencies', 'required': True}),
            'tags': forms.TextInput(attrs={'class': 'w-full border border-black rounded-lg p-2', 'placeholder': 'Enter Tags (comma-separated)', 'required': True}),
            'company_logo': forms.FileInput(attrs={'class': 'block w-full text-black', 'required': True}),
        }

