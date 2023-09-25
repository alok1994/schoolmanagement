from django.shortcuts import render, redirect
from .models import Fee
from .forms import FeeForm
from admissions.models import Admission  # Import the Student model

def fee_detail(request):
    # Get a list of distinct class values from the Student model
    class_choices = Admission.objects.values_list('admission_class', flat=True).distinct()
    print(class_choices)
    selected_class = request.GET.get('class_filter')  # Get the selected class from the query parameter
    print(selected_class)
    # Filter fees based on the selected class (if provided)
    if selected_class:
        #import pdb;pdb.set_trace()
        class_students = Admission.objects.filter(admission_class=selected_class)
        print(class_students)
    #else:
    #    fees = Fee.objects.all()
    #    print(fees)
    print(class_students)
    return render(request, 'fee_management/fee_detail.html', {'class_students': class_students, 'class_choices': class_choices, 'selected_class': selected_class})


def add_fee(request):
    if request.method == 'POST':
        form = FeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fee_detail')  # Redirect to the fee details page
    else:
        form = FeeForm()
    return render(request, 'fee_management/add_fee.html', {'form': form})
