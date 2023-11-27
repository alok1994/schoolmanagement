from django.shortcuts import render, redirect, get_object_or_404
from .models import Fee
from .forms import FeeForm
from admissions.models import Admission  # Import the Student model
from django.db.models import Max
from datetime import datetime
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from num2words import num2words

@login_required
def fee_detail(request):
    # Get a list of distinct class values from the Student model
    class_choices = Admission.objects.values_list('admission_class', flat=True).distinct()
    selected_class = request.GET.get('class_filter')  # Get the selected class from the query parameter
    # Filter fees based on the selected class (if provided)
    if selected_class:
        class_students = Admission.objects.filter(admission_class=selected_class)
    else:
        class_students = Admission.objects.all()

    # Pagination
    page = request.GET.get('page')
    paginator = Paginator(class_students, 20)  # Display 10 students per page, you can adjust this number as needed

    class_students = paginator.get_page(page)

    last_month_fees = Fee.objects.filter(student__in=Admission.objects.all()).values('student').annotate(
        last_month=Max('fee_for_month'),
        last_month_amount=Max('tuition_fee'),
        last_month_payment_date=Max('payment_date')
    )

    # Create a dictionary mapping student IDs to their last month's fee data
    last_month_fee_dict = {}
    for fee in last_month_fees:
        student_id = fee['student']
        last_month_fee_dict[student_id] = {
            'last_month': fee['last_month'],
            'last_month_amount': fee['last_month_amount'],
            'last_month_payment_date': fee['last_month_payment_date']
        }

    last_month_fee_list = []

    for student in class_students:
        student_id = student.id
        last_month_data = last_month_fee_dict.get(student_id, {})
        last_month_fee_list.append((student, last_month_data))

    return render(request, 'fee_management/fee_detail.html', {'class_students': class_students, 'class_choices': class_choices, 'selected_class': selected_class, 'last_month_fee_list': last_month_fee_list})

@login_required
def fee_submission(request, student_id):
    try:
        student = Admission.objects.get(id=student_id)  # Retrieve the student using student_id
    except student.DoesNotExist:
        # Handle the case where the student with the given ID does not exist
        # You can raise an error, redirect to an error page, or handle it as needed
        return redirect('error_page')  # Replace 'error_page' with your desired URL name
    #import pdb;pdb.set_trace()
    if request.method == 'POST':
        fee_form = FeeForm(request.POST)
        if fee_form.is_valid():
            fee = fee_form.save(commit=False)
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            random_part = get_random_string(length=6, allowed_chars='1234567890')
            receipt_number = f"R{timestamp}{random_part}"

            fee.registration_fee = fee.registration_fee or 0
            fee.tuition_fee = fee.tuition_fee or 0
            fee.exam_fee = fee.exam_fee or 0
            fee.sports_fee = fee.sports_fee or 0
            fee.miscellaneous_fee = fee.miscellaneous_fee or 0
            fee.late_fee = fee.late_fee or 0
            fee.discount_fee = fee.discount_fee or 0

            total_paid_amount = (
                fee.registration_fee + fee.tuition_fee + fee.exam_fee +
                fee.sports_fee + fee.miscellaneous_fee - fee.discount_fee + fee.late_fee
            )

            fee.total_paid_amount = total_paid_amount

            #fee.class = student.current_class

            fee.total_amount_in_words = num2words(total_paid_amount, lang='en_IN').title()

            #fee_history = Fee.objects.filter(student=student).order_by('-payment_date')

            # Get the student's current semester from the AdmissionForm
            #current_semester = student.current_class

            #try:
            #    semester_fee = Semester.objects.get(semester_number=student.current_semester)
            #    total_semester_fee = semester_fee.semester_total
            #    fee.total_semester_fee = total_semester_fee
            #except Semester.DoesNotExist:
            #    total_semester_fee = 0

            fee = fee_form.save(commit=False)
            fee.student = student
            fee.receipt_number = receipt_number
            fee.save()
            print(f"Fee ID: {fee.id}")
            return redirect('generate_receipt', fee.id)
        else:
            print(fee_form.errors)
    else:
        fee_form = FeeForm()

    return render(request, 'fee_management/fee_submission.html', {'fee_form': fee_form, 'student': student})

@login_required
def fee_history(request, student_id):
    student = get_object_or_404(Admission, id=student_id)  # Get the student by ID

    # Query the database to get the fee history for the selected student
    fee_history = Fee.objects.filter(student=student).order_by('-payment_date')

    # Configure the pagination
    page = request.GET.get('page')
    paginator = Paginator(fee_history, 10)  # Show 10 fee entries per page

    try:
        fee_history = paginator.page(page)
    except PageNotAnInteger:
        fee_history = paginator.page(1)
    except EmptyPage:
        fee_history = paginator.page(paginator.num_pages)

    return render(request, 'fee_management/fee_history.html', {'student': student, 'fee_history': fee_history})
@login_required
def generate_receipt(request, fee_id):
    fee = get_object_or_404(Fee, id=fee_id)
    student = fee.student

    context = {
        'student': student,
        'fee': fee,
    }

    return render(request, 'fee_management/receipt.html', context)