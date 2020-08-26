from django import forms
from .models import Invitation


class CridentialsForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ['name', 'email']
