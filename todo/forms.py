from dataclasses import field
from django import forms
from .models import TODOS

class ListForms(forms.ModelForm):
    class Meta:
        model = TODOS
        fields = ["title", "description", "is_finished", "create_date"]