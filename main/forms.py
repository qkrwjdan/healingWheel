from django import forms
from .models import DrivingTime

class DrivingTimeForm(forms.ModelForm):
    class Meta:
        model = DrivingTime
        fields = ('detail_menu',)
