from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['phone_number', 'cover_letter']
        widgets = {
            'phone_number': forms.TextInput(attrs={
                'class': 'profile_edit_input',
                'name': 'phone_number',
                'placeholder': '0912345...',
                'type': 'tel',
                'pattern': '^9[0-9]{9}$',
                'title': 'Enter a valid 10-digit cellphone number starting with 9',
                'required': True
            }),
            'cover_letter': forms.Textarea(attrs={
                'class': 'w-full h-48 mt-4 rounded-2xl border-2 border-gray-300',
                'name': 'cover_letter',
                'placeholder': 'I think I am fit for this job because...',
            })
        }
    def __init__(self, *args, user=None, form=None, **kwargs):
        super().__init__(*args, **kwargs)
        # optional letter
        self.fields['cover_letter'].required = False

        if user:
            if user.is_authenticated:
                self.fields['phone_number'].initial = user.phone_number
                if user.phone_number:
                    self.fields['phone_number'].widget.attrs['readonly'] = True
            
            if form:
                self.fields['phone_number'].initial = form.phone_number
                self.fields['cover_letter'].initial = form.cover_letter