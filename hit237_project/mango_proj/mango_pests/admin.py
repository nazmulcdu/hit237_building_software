from django.contrib import admin
from .models import Pest, Symptom, Treatment

# Registering Pest model
@admin.register(Pest)
class PestAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name')
    search_fields = ('name', 'scientific_name', 'short_desc', 'full_desc')
    list_filter = ('name',)

# Registering Symptom model
@admin.register(Symptom)
class SymptomAdmin(admin.ModelAdmin):
    list_display = ('pest', 'affected_part', 'description')
    search_fields = ('pest__name', 'affected_part')
    list_filter = ('pest',)

# Registering Treatment model
@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('pest', 'name', 'is_organic')
    search_fields = ('pest__name', 'name')
    list_filter = ('is_organic', 'pest')
