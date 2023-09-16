# Generated by Django 4.2.5 on 2023-09-10 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admission_form', '0002_alter_admissionform_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_year', models.PositiveIntegerField()),
                ('student_name', models.PositiveIntegerField()),
                ('admission_form', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admission_form.admissionform')),
            ],
        ),
    ]
