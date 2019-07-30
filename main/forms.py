from django import forms
from .models import DrivingTime,Profile

class DrivingTimeForm(forms.ModelForm):
    class Meta:
        model = DrivingTime
        fields = ('detail_menu',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('duration',)
