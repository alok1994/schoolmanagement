# admissions/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AdmissionForm
from .models import Admission
from .forms import AdmissionYearFilterForm, AdmissionClassFilterForm

def admission_form(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = AdmissionForm()
    return render(request, 'admissions/admission_form.html', {'form': form})

def student_list(request):
    students = Admission.objects.all()

    # Apply filters if provided in the GET request
    year_filter_form = AdmissionYearFilterForm(request.GET)
    if year_filter_form.is_valid():
        admission_year = year_filter_form.cleaned_data.get('admission_year')
        if admission_year:
            students = students.filter(admission_date__year=admission_year)

    class_filter_form = AdmissionClassFilterForm(request.GET)
    if class_filter_form.is_valid():
        admission_class = class_filter_form.cleaned_data.get('admission_class')
        if admission_class:
            students = students.filter(admission_class__icontains=admission_class)

    context = {
        'students': students,
        'year_filter_form': year_filter_form,
        'class_filter_form': class_filter_form,
    }

    return render(request, 'admissions/student_list.html', context)

def student_details(request, student_id):
    student = get_object_or_404(Admission, pk=student_id)
    return render(request, 'admissions/student_details.html', {'student': student})

def dashboard(request):
    return render(request, 'admissions/dashboard.html')


def class_6(request):
    class_6_students = Admission.objects.filter(admission_class='6')

    # Handle year filter
    year_filter_form = AdmissionYearFilterForm(request.GET)
    if year_filter_form.is_valid():
        admission_year = year_filter_form.cleaned_data.get('admission_year')
        if admission_year:
            class_6_students = class_6_students.filter(admission_date__year=admission_year)

    context = {
        'class_6_students': class_6_students,
        'year_filter_form': year_filter_form,
    }
    return render(request, 'admissions/class_6.html', context)

def class_7(request):
    class_7_students = Admission.objects.filter(admission_class='7')
    year_filter_form = AdmissionYearFilterForm(request.GET)
    if year_filter_form.is_valid():
        admission_year = year_filter_form.cleaned_data.get('admission_year')
        if admission_year:
            class_7_students = class_7_students.filter(admission_date__year=admission_year)

    context = {
        'class_7_students': class_7_students,
        'year_filter_form': year_filter_form,
    }
    return render(request, 'admissions/class_7.html', context)

def class_8(request):
    class_8_students = Admission.objects.filter(admission_class='8')
    year_filter_form = AdmissionYearFilterForm(request.GET)
    if year_filter_form.is_valid():
        admission_year = year_filter_form.cleaned_data.get('admission_year')
        if admission_year:
            class_8_students = class_8_students.filter(admission_date__year=admission_year)

    context = {
        'class_8_students': class_8_students,
        'year_filter_form': year_filter_form,
    }
    return render(request, 'admissions/class_8.html', context)

def class_9(request):
    class_9_students = Admission.objects.filter(admission_class='9')
    year_filter_form = AdmissionYearFilterForm(request.GET)
    if year_filter_form.is_valid():
        admission_year = year_filter_form.cleaned_data.get('admission_year')
        if admission_year:
            class_9_students = class_9_students.filter(admission_date__year=admission_year)

    context = {
        'class_9_students': class_9_students,
        'year_filter_form': year_filter_form,
    }
    return render(request, 'admissions/class_9.html', context)

def class_10(request):
    class_10_students = Admission.objects.filter(admission_class='10')
    year_filter_form = AdmissionYearFilterForm(request.GET)
    if year_filter_form.is_valid():
        admission_year = year_filter_form.cleaned_data.get('admission_year')
        if admission_year:
            class_10_students = class_10_students.filter(admission_date__year=admission_year)

    context = {
        'class_10_students': class_10_students,
        'year_filter_form': year_filter_form,
    }
    return render(request, 'admissions/class_10.html', context)

def class_11(request):
    class_11_students = Admission.objects.filter(admission_class='11')
    year_filter_form = AdmissionYearFilterForm(request.GET)
    if year_filter_form.is_valid():
        admission_year = year_filter_form.cleaned_data.get('admission_year')
        if admission_year:
            class_11_students = class_11_students.filter(admission_date__year=admission_year)

    context = {
        'class_11_students': class_11_students,
        'year_filter_form': year_filter_form,
    }
    return render(request, 'admissions/class_11.html', context)

def class_12(request):
    class_12_students = Admission.objects.filter(admission_class='12')
    year_filter_form = AdmissionYearFilterForm(request.GET)
    if year_filter_form.is_valid():
        admission_year = year_filter_form.cleaned_data.get('admission_year')
        if admission_year:
            class_12_students = class_12_students.filter(admission_date__year=admission_year)

    context = {
        'class_12_students': class_12_students,
        'year_filter_form': year_filter_form,
    }
    return render(request, 'admissions/class_12.html', context)


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

