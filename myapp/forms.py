# core/forms.py
from django import forms
from .models import UploadedFile

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']

class QueryForm(forms.Form):
    keyword = forms.CharField(label='Keyword', required=False)
    industry = forms.CharField(label='Industry', required=False)
    year_founded = forms.IntegerField(label='Year Founded', required=False)
    city = forms.CharField(label='City', required=False)
    state = forms.CharField(label='State', required=False)
    country = forms.CharField(label='Country', required=False)
    employees_from = forms.IntegerField(label='Employees (From)', required=False)
    employees_to = forms.IntegerField(label='Employees (To)', required=False)
