from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path('', views.leads_page, name='lead-list'),
    path('create/', views.lead_create_form, name='create-lead'),
    path('detail/<int:pk>/', views.lead_detail, name='lead-detail'),
    path('delete/<int:pk>/', views.lead_delete, name='delete-lead'),
    path('update/<int:pk>/', views.lead_update, name='update-lead'),
]