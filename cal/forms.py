from django import forms
from .models import Income,spending

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ('name','money')


class SpendForm(forms.ModelForm):
    class Meta:
        model = spending
        fields = ('name','money')
