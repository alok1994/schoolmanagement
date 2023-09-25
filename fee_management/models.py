from django.db import models

class Fee(models.Model):
    student = models.ForeignKey('admissions.Admission', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    # Add more fields as needed
