# Generated by Django 4.2.5 on 2023-09-26 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fee_management', '0002_fee_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='receipt_number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]