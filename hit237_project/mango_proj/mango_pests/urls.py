from django.urls import path
from .views import pest_list  # Relative import

urlpatterns = [
    path('pests/', pest_list, name='pest-list'),  # Just app-specific URLs
]