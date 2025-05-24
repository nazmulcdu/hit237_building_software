from django.contrib import admin
from .models.pest_model import PestDisease, Grower, Plant, Surveillance

@admin.register(PestDisease)
class PestDiseaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'brief_desc')
    search_fields = ('name', 'brief_desc', 'full_desc', 'symptoms')
    list_filter = ('name',)

    def changelist_view(self, request, extra_context=None):
        mango_count = PestDisease.objects.filter(name__icontains="mango").count()
        if extra_context is None:
            extra_context = {}
        extra_context['mango_disease_count'] = mango_count
        return super().changelist_view(request, extra_context=extra_context)

@admin.register(Grower)
class GrowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'property_location', 'stock_rate')
    search_fields = ('name', 'property_location')

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    search_fields = ('name', 'type')

@admin.register(Surveillance)
class SurveillanceAdmin(admin.ModelAdmin):
    list_display = ('grower', 'plant', 'pest_disease', 'surveyed_part', 'location', 'time_of_survey', 'result')
    search_fields = ('grower__name', 'plant__name', 'pest_disease__name', 'location', 'surveyed_part')
    list_filter = ('grower', 'plant', 'pest_disease', 'location', 'time_of_survey')
