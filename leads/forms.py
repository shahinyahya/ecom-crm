from django import forms
from django.forms import widgets
from .models import Lead

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