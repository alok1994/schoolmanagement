from django.shortcuts import render, redirect, get_object_or_404
from .models import Fee
from .forms import FeeForm
from admissions.models import Admission  # Import the Student model
from django.db.models import Max
from datetime import datetime
from django.utils.crypto import get_random_string


def fee_detail(request):
    # Get a list of distinct class values from the Student model
    class_choices = Admission.objects.values_list('admission_class', flat=True).distinct()
    selected_class = request.GET.get('class_filter')  # Get the selected class from the query parameter
    # Filter fees based on the selected class (if provided)
    if selected_class:
        #import pdb;pdb.set_trace()
        class_students = Admission.objects.filter(admission_class=selected_class)
        print(class_students)
    else:
        class_students = Admission.objects.all()
    #    print(fees)
    last_month_fees = Fee.objects.filter(student__in=Admission.objects.all()).values('student').annotate(last_month=Max('month'), last_month_amount=Max('amount'), last_month_payment_date=Max('payment_date'))

    # Create a dictionary mapping student IDs to their last month's fee data
    last_month_fee_dict = {}
    for fee in last_month_fees:
        student_id = fee['student']
        last_month_fee_dict[student_id] = {
            'last_month': fee['last_month'],
            'last_month_amount': fee['last_month_amount'],
            'last_month_payment_date': fee['last_month_payment_date']
        }

    #current_month_fees = Fee.objects.filter(student__in=Admission.objects.all()).values('student').annotate(
    #    current_month=Max('month'),
    #    current_month_amount=Max('amount')
    #)

    #current_month_fee_dict = {}
    #for fee in current_month_fees:
    #    student_id = fee['student']
    #    current_month_fee_dict[student_id] = {
    #        'current_month': fee['current_month'],
    #        'current_month_amount': fee['current_month_amount']
    #    }
    
    last_month_fee_list = []
    #current_month_fee_list = []
    for student in class_students:
        student_id = student.id
        last_month_data = last_month_fee_dict.get(student_id, {})
        #current_month_data = current_month_fee_dict.get(student_id, {})
        last_month_fee_list.append((student, last_month_data))
        #current_month_fee_list.append((student, current_month_data))

    return render(request, 'fee_management/fee_detail.html', {'class_students': class_students, 'class_choices': class_choices, 'selected_class': selected_class, 'last_month_fee_list': last_month_fee_list,})


def fee_submission(request, student_id):
    try:
        student = Admission.objects.get(id=student_id)  # Retrieve the student using student_id
    except Student.DoesNotExist:
        # Handle the case where the student with the given ID does not exist
        # You can raise an error, redirect to an error page, or handle it as needed
        return redirect('error_page')  # Replace 'error_page' with your desired URL name

    if request.method == 'POST':
        fee_form = FeeForm(request.POST)
        if fee_form.is_valid():
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            random_part = get_random_string(length=6, allowed_chars='1234567890')
            receipt_number = f"R{timestamp}{random_part}"
            fee = fee_form.save(commit=False)
            fee.student = student
            fee.receipt_number = receipt_number
            fee.save()
            print(f"Fee ID: {fee.id}")
            return redirect('generate_receipt', fee.id)
    else:
        fee_form = FeeForm()

    return render(request, 'fee_management/fee_submission.html', {'fee_form': fee_form, 'student': student})

def fee_history(request, student_id):
    student = get_object_or_404(Admission, id=student_id)  # Get the student by ID

    # Query the database to get the fee history for the selected student
    fee_history = Fee.objects.filter(student=student).order_by('-payment_date')

    return render(request, 'fee_management/fee_history.html', {'student': student, 'fee_history': fee_history})

def generate_receipt(request, fee_id):
    fee = get_object_or_404(Fee, id=fee_id)
    student = fee.student

    context = {
        'student': student,
        'fee': fee,
    }

    return render(request, 'fee_management/receipt.html', context)