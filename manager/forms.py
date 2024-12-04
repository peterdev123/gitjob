from django import forms
from .models import JobPost

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['job_title', 'job_field', 'job_schedule', 'address', 'hiring_deadline', 
                  'min_salary', 'max_salary', 'job_description', 'company_name',
                  'core_competencies', 'tags', 'company_logo']
        
        widgets = {
            'job_title': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-3 bg-gray-50 focus:ring-2 focus:ring-blue-500 focus:outline-none', 
                'placeholder': 'Enter Job Title', 
                'required': True
            }),
            'company_name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-3 bg-gray-50 focus:ring-2 focus:ring-blue-500 focus:outline-none',
                'placeholder': 'Enter Company Name',
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