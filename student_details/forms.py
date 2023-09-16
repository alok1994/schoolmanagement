# student_details/forms.py
from django import forms
from .models import Student

class StudentSearchForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['current_year']  # Add other fields as needed for searching
