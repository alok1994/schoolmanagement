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

class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ['first_name', 'middle_name', 'last_name', 'father_name', 'mother_name', 'aadhar_card', 'admission_class', 'mobile_number']