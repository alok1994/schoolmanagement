# Generated by Django 4.2.5 on 2023-09-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0002_admission_mobile_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='subjects',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
