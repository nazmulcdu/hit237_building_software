from django import forms
from .models import PestReport

class PestReportForm(forms.ModelForm):
    class Meta:
        model = PestReport
        fields = ['full_name', 'email', 'location', 'pest_name', 'observation', 'image']
