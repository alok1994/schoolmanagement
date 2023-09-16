# admission_form/models.py
from django.db import models

class AdmissionForm(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cast = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    admission_date = models.CharField(max_length=20)
    address = models.TextField(max_length=1000)
    photo = models.CharField(max_length=1000)
    aadhar_card_number = models.CharField(max_length=12, unique=True)
    mobile_number = models.CharField(max_length=10)
    previous_school_details = models.TextField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
