from django import forms
from .models import NewRequest

class NewRequestForm(forms.ModelForm):
    class Meta:
        model = NewRequest
        fields = ['title', 'description', 'location', 'request_type']
