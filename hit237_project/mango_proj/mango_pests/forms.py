from django import forms
from .models import Farmer, Treatment, PestReport


class FarmerFarmForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['full_name', 'email', 'phone_number', 'location', 'land_size']

class PestDetailsForm(forms.ModelForm):
    class Meta:
        model = PestReport
        fields = ['pest_name', 'date_of_observation', 'observation', 'severity_level',
                  'affected_stage', 'affected_plant_number', 'symptoms', 'image']
        widgets = {
            'date_of_observation': forms.DateInput(attrs={'type': 'date'}),
        }

class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = [
            'treatment_type',
            'product_name',
            'application_method',
            'application_date',
            'is_organic',
        ]
        widgets = {
            'application_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
        'treatment_type': 'Treatment Type','product_name': 'Product Name',
        'application_method': 'Application Method','application_date': 'Application Date',
        'is_organic': 'Is Organic?',
        }
