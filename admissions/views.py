# admissions/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AdmissionForm
from .models import Admission

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
    return render(request, 'admissions/student_list.html', {'students': students})

def student_details(request, student_id):
    student = get_object_or_404(Admission, pk=student_id)
    return render(request, 'admissions/student_details.html', {'student': student})