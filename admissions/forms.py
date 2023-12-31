# admissions/forms.py
from django import forms
from .models import Admission

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        exclude = ['current_class']

    photo = forms.ImageField(required=False)
    
class AdmissionYearFilterForm(forms.Form):
    admission_year = forms.IntegerField(label='Year of Admission', required=False)

class AdmissionClassFilterForm(forms.Form):
    admission_class = forms.CharField(label='Admission Class', required=False)

class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Admission
        exclude = ['admission_class']

# Ensure enctype attribute is set for file uploads
StudentUpdateForm.base_fields['photo'].widget.attrs.update({'enctype': 'multipart/form-data'})