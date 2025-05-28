from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from .pest_data import mango_pestdiseases
from .forms import FarmerFarmForm, PestDetailsForm, TreatmentForm
from .models import Farmer, Pest, Treatment, PestReport
from django.urls import reverse_lazy
from django.views.generic import (ListView, UpdateView, DeleteView)


def home(request):
    return render(request, 'mango_pests/home.html')

def about(request):
    return render(request, 'mango_pests/about.html')

def pest_list(request):
    return render(request, 'mango_pests/list.html', {'pests': mango_pestdiseases})

def pest_detail(request, slug):
    pest = next((p for p in mango_pestdiseases if p.slug == slug), None)
    if not pest:
        return render(request, 'mango_pests/not_found.html', status=404)
    return render(request, 'mango_pests/detail.html', {'pest': pest})

def pest_list_view(request):
    return render(request, 'pests.html', {'pests': mango_pestdiseases})

def preventive_tips(request):
    return render(request, 'mango_pests/preventive_tips.html')

def report_pest(request):
    if request.method == 'POST':
        farmer_form = FarmerFarmForm(request.POST)
        pest_form = PestDetailsForm(request.POST, request.FILES)
        treatment_form = TreatmentForm(request.POST)

        if farmer_form.is_valid() and pest_form.is_valid() and treatment_form.is_valid():
            farmer = farmer_form.save()
            pest = pest_form.save(commit=False)
            pest.farmer = farmer
            pest.save()

            treatment = treatment_form.save(commit=False)
            treatment.pest_report = pest
            treatment.save()

            return render(request, 'mango_pests/confirmation.html')
    else:
        farmer_form = FarmerFarmForm()
        pest_form = PestDetailsForm()
        treatment_form = TreatmentForm()

    return render(request, 'mango_pests/userform.html', {
        'farmer_form': farmer_form,
        'pest_form': pest_form,
        'treatment_form': treatment_form,
    })

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'mango_pests/signup.html', {'form': form})

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
class PestReportListView(ListView):
    model = PestReport
    template_name = 'mango_pests/survey_list.html'
    context_object_name = 'pestreports'

class PestReportUpdateView(UpdateView):
        model = PestReport
        template_name = 'mango_pests/edit.html'
        fields = ['pest_name', 'affected_stage', 'observation', 'date_of_observation', 'farmer']
        success_url = reverse_lazy('pestreport_list')

class PestReportDeleteView(DeleteView):
    model = PestReport
    template_name = 'mango_pests/delete.html'
    success_url = reverse_lazy('pestreport_list')


