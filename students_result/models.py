from django.db import models
from admissions.models import Admission  # Import the Admission model from the admissions app

class Result(models.Model):
    student = models.ForeignKey(Admission, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    min_marks = models.DecimalField(max_digits=5, decimal_places=2)
    max_marks = models.DecimalField(max_digits=5, decimal_places=2)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    remark = models.CharField(max_length=255)
    exam_type = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.subject}"
