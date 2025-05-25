from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pests/', views.pest_list, name='pest_list'),
    re_path(r'^pests/(?P<slug>[\w-]+)/$', views.pest_detail, name='pest_detail'),
    path('report/', views.report_pest, name='report_pest'),
    path('preventive-tips/', views.preventive_tips, name='preventive_tips'),
    path('report/<int:pk>/edit/', views.report_edit, name='report_edit'),
    path('report/<int:pk>/delete/', views.report_delete, name='report_delete'),

]
