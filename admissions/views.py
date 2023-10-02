from django.shortcuts import render, redirect, get_object_or_404
from .forms import AdmissionForm
from .models import Admission
from .forms import AdmissionYearFilterForm, AdmissionClassFilterForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import StudentUpdateForm

@login_required
def admission_form(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = AdmissionForm()
    return render(request, 'admissions/admission_form.html', {'form': form})

@login_required
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

@login_required
def student_details(request, student_id):
    student = get_object_or_404(Admission, pk=student_id)
    return render(request, 'admissions/student_details.html', {'student': student})

@login_required
def dashboard(request):
    return render(request, 'admissions/dashboard.html')

@login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
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


@login_required
def get_student_data(request):
    # Query your Admission model to retrieve student data
    students = Admission.objects.all()
    
    # Serialize the data to JSON
    student_data = [
        {
            'first_name': student.first_name,
            'middle_name': student.middle_name,
            'last_name': student.last_name,
            'admission_class': student.admission_class,
        }
        for student in students
    ]
    
    # Return the JSON response
    return JsonResponse(student_data, safe=False)


@login_required
def update_student(request, student_id):
    student = get_object_or_404(Admission, id=student_id)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect back to the student list page
    else:
        form = StudentUpdateForm(instance=student)

    context = {
        'student': student,
        'form': form,
    }

    return render(request, 'admissions/update_student.html', context)


