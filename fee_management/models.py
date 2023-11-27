from django.db import models

class Fee(models.Model):
    student = models.ForeignKey('admissions.Admission', on_delete=models.CASCADE)
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    exam_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sports_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    miscellaneous_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_date = models.DateField()
    fee_for_month = models.CharField(max_length=255)
    receipt_number = models.CharField(max_length=20)
    late_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    current_class = models.CharField(max_length=255)
    total_paid_amount =  models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_amount_in_words = models.CharField(max_length=10000)


    # Add more fields as needed

    def __str__(self):
        return f"Receipt #{self.receipt_number} - {self.student.fist_name} - {self.fee_for_month}"