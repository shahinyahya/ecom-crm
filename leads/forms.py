from django import forms
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordResetView
from .models import Lead

User = get_user_model()
class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
        )
        widgets = {
            # 'first_name': widgets.TextInput(attrs=),
            'agent': widgets.Select()
        }

class LeadUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age'
        )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}