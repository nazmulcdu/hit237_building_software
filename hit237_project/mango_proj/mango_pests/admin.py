from django.contrib import admin
from .models import Farmer, Pest, Treatment, PestReport

# Registering Pest model
@admin.register(Pest)
class PestAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name')
    search_fields = ('name', 'scientific_name', 'short_desc', 'full_desc')
    list_filter = ('name',)

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'location', 'land_size')
    search_fields = ('full_name', 'location', 'email')
    list_filter = ('location',)

@admin.register(PestReport)
class PestReportAdmin(admin.ModelAdmin):
    list_display = ('pest_name', 'farmer', 'date_of_observation', 'severity_level', 'affected_stage')
    search_fields = ('pest_name', 'farmer__full_name', 'observation')
    list_filter = ('severity_level', 'affected_stage', 'date_of_observation')

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('pest_report', 'product_name', 'treatment_type', 'application_method', 'application_date', 'is_organic')
    search_fields = ('pest_report__pest_name', 'product_name')
    list_filter = ('treatment_type', 'application_method', 'is_organic', 'application_date')

