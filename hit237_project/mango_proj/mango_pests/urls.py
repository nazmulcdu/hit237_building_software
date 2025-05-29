from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLogoutView
from .views import PestReportListView
from .views import PestReportUpdateView


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='mango_pests/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', views.signup_view, name='signup'),

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pests/', views.pest_list, name='pest_list'),
    re_path(r'^pests/(?P<slug>[\w-]+)/$', views.pest_detail, name='pest_detail'),
    path('report/', views.report_pest, name='report_pest'),
    path('preventive-tips/', views.preventive_tips, name='preventive_tips'),
    #path('report/<int:pk>/edit/', views.report_edit, name='report_edit'),
    #path('report/<int:pk>/delete/', views.report_delete, name='report_delete'),
    path('survey_list/', PestReportListView.as_view(), name='pestreport_list'),
    path('survey_list/<int:pk>/edit/', PestReportUpdateView.as_view(), name='pestreport_edit'),
    path('survey_list/<int:pk>/delete/', views.PestReportDeleteView.as_view(), name='pestreport_delete'),
]
