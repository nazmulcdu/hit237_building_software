# mango_proj/urls.py
from django.contrib import admin
from django.urls import path
from mango_pests.views import pest_list 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pests/', pest_list, name='pest-list'),
]