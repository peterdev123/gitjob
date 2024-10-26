from django import forms
from .models import JobPost

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['job_title', 'job_field', 'address', 'hiring_deadline', 
                  'min_salary', 'max_salary', 'job_description', 
                  'core_competencies', 'tags', 'company_logo']
        
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'w-full border border-black rounded-lg p-2', 'placeholder': 'Enter Job Title'}),
            'job_field': forms.TextInput(attrs={'class': 'w-full border border-black rounded-lg p-2', 'placeholder': 'Enter Job Field'}),
            'address': forms.TextInput(attrs={'class': 'w-full border border-black rounded-lg p-2', 'placeholder': 'Enter Company Address'}),
            'hiring_deadline': forms.DateInput(attrs={'class': 'w-full border border-black rounded-lg p-2', 'type': 'date'}),
            'min_salary': forms.NumberInput(attrs={'class': 'w-full border border-black rounded-lg p-2', 'placeholder': 'Enter Minimum Salary'}),
            'max_salary': forms.NumberInput(attrs={'class': 'w-full border border-black rounded-lg p-2', 'placeholder': 'Enter Maximum Salary'}),
            'job_description': forms.Textarea(attrs={'class': 'w-full border border-black rounded-lg p-2', 'rows': 4, 'placeholder': 'Enter Job Description'}),
            'core_competencies': forms.Textarea(attrs={'class': 'w-full border border-black rounded-lg p-2', 'rows': 3, 'placeholder': 'Enter Core Competencies'}),
            'tags': forms.TextInput(attrs={'class': 'w-full border border-black rounded-lg p-2', 'placeholder': 'Enter Tags (comma-separated)'}),
            'company_logo': forms.FileInput(attrs={'class': 'block w-full text-black'}),
        }