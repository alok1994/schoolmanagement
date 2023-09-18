# admissions/forms.py
from django import forms
from .models import Admission

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = '__all__'

class AdmissionYearFilterForm(forms.Form):
    admission_year = forms.IntegerField(label='Year of Admission', required=False)

class AdmissionClassFilterForm(forms.Form):
    admission_class = forms.CharField(label='Admission Class', required=False)