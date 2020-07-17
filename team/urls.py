from django.urls import path
from . import views

app_name= 'member_urls'

urlpatterns = [
  path('', views.all_members, name= 'all_members'),
  path('<int:member_id>/', views.member_detail, name= 'member_detail'),
]