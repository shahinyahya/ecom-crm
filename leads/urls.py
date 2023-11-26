from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    # path('', views.leads_page, name='lead-list'),
    # path('create/', views.lead_create_form, name='create-lead'),
    # path('<int:pk>/', views.lead_detail, name='lead-detail'),
    # path('<int:pk>/update', views.lead_update, name='update-lead'),
    # path('<int:pk>/delete', views.lead_delete, name='delete-lead'),

    # Class Based views urls
    path('', views.LeadListView.as_view(), name='lead-list'),
    path('create/', views.LeadCreateView.as_view(), name='create-lead'),
    path('<int:pk>/', views.LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update', views.LeadUpdateView.as_view(), name='update-lead'),
    path('<int:pk>/delete', views.LeadDeleteView.as_view(), name='delete-lead'),
]