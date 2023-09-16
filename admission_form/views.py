# admission_form/views.py
from django.shortcuts import render, redirect
from .models import AdmissionForm
from .forms import AdmissionForm as AdmissionFormModelForm

def admission_form(request):
    if request.method == 'POST':
        form = AdmissionFormModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a success page or the dashboard
            return redirect('dashboard')  # Change 'dashboard' to the actual dashboard URL name
    else:
        form = AdmissionFormModelForm()
    return render(request, 'admission_form/admission_form.html', {'form': form})
