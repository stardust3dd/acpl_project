from django.urls import path
from . import views

app_name= 'cases_urls'

urlpatterns = [
  path('', views.all_cases, name= 'all_cases'),
  path('<int:case_id>/', views.case_detail, name= 'case_detail'),
]