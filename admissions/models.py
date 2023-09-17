# admissions/models.py
from django.db import models

class Admission(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    aadhar_card = models.CharField(max_length=16)
    photo = models.ImageField(upload_to='photos/')
    previous_school = models.CharField(max_length=200)
    address = models.TextField()
    caste = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
