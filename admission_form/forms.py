# admission_form/forms.py
from django import forms
from .models import AdmissionForm

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = AdmissionForm
        fields = '__all__'
