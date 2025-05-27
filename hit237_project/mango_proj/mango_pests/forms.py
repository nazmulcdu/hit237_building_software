from django import forms
from .models import PestReport

class PestReportForm(forms.ModelForm):
    class Meta:
        model = PestReport
        fields = ['full_name', 'email', 'phone_number', 'location', 'land_size', 'pest_name', 'date_of_observation', 'observation', 'severity_level', 'affected_stage', 'affected_farm_area', 'symptoms','image']

        widgets= {
            'date_of_observation': forms.DateInput(attrs={'type':'date'}),
        }
