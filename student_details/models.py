# student_details/models.py
from django.db import models
from admission_form.models import AdmissionForm

class Student(models.Model):
    admission_form = models.OneToOneField(AdmissionForm, on_delete=models.CASCADE)
    current_year = models.PositiveIntegerField()
    student_name = models.PositiveIntegerField()
    # Add other student details as needed (e.g., Photo, Student Name, Father Name, Mother Name, Mobile Number)
