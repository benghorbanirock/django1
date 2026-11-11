from django import forms
from .models import Reservetion

class ReservetionForm(forms.ModelForm):
    class Meta:
        model=Reservetion
        fields='__all__'