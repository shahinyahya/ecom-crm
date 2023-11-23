from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path('', views.home_page, name='home'),
    path('leads/', views.leads_page, name='lead-list'),
    path('leads/create/', views.lead_create_form, name='create-lead'),
    path('leads/<int:pk>/update', views.lead_update, name='update-lead'),
    path('leads/<int:pk>/delete/', views.lead_delete, name='delete-lead')
]