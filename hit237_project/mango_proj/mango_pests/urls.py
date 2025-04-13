from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pests/', views.pest_list, name='pest_list'),
    re_path(r'^pests/(?P<slug>[\w-]+)/$', views.pest_detail, name='pest_detail'),
]
