from django.shortcuts import render,redirect
from .models import Result
from admissions.models import Admission

def students_result(request):
    # Handle filtering based on class (admission_class)
    class_choices = Admission.objects.values_list('admission_class', flat=True).distinct()
    selected_class = request.GET.get('class_filter')
    if selected_class:
        results = Admission.objects.filter(admission_class=selected_class)
        print(results)
    else:
        results = Admission.objects.all()

    return render(request, 'students_result/students_result.html', {'results': results, 'class_choices': class_choices, 'selected_class': selected_class})


def create_result(request, student_id):
    student = Admission.objects.get(id=student_id)

    if request.method == 'POST':
        # Retrieve form data for each subject
        subjects = ['hindi', 'english', 'maths', 'science', 'ss', 'sankarit', 'geology', 'arts']
        total_max_marks = 0  # Initialize total max marks
        total_marks_obtained = 0  # Initialize total marks obtained
        percentage = 0
        result_objects = []

        for subject in subjects:
            min_marks = request.POST.get(f'min_marks_{subject}')
            max_marks = request.POST.get(f'max_marks_{subject}')
            marks = request.POST.get(f'marks_{subject}')
            remark = request.POST.get(f'remark_{subject}')
            exam_type = request.POST.get('exam_type')    
            total_max_marks += int(max_marks)
            total_marks_obtained += int(marks)
            total_min_marks += int(min_marks)
            
            # Create a Result object but don't save it yet
            result = Result(
                student=student,
                subject=subject.capitalize(),  # Capitalize the subject name
                min_marks=min_marks,
                max_marks=max_marks,
                marks_obtained=marks,
                remark=remark,
                exam_type =exam_type,
            )
            result_objects.append(result)

        if total_max_marks > 0:
            percentage = (total_marks_obtained / total_max_marks) * 100
        else:
            percentage = 0

        Result.objects.bulk_create(result_objects)

        # Now, create and save the total result with percentage
        total_result = Result(
            student=student,
            subject='Total',  # You can use a special subject name like 'Total'
            min_marks=total_min_marks,  # Set min marks for the total as 0
            max_marks=total_max_marks,
            marks_obtained=total_marks_obtained,
            remark='',  # You can leave the remark empty for the total
            percentage=percentage,
        )
        total_result.save()
        return redirect('students_result')

    return render(request, 'students_result/create_result.html', {'student': student})


def result_history(request, student_id):
    # Retrieve the student
    student = Admission.objects.get(id=student_id)

    # Get the selected exam type from the request
    exam_type = request.GET.get('exam_type', '')  # Default to empty string if not provided

    # Filter the result history based on the selected exam type
    result_history = Result.objects.filter(student=student)
    if exam_type:
        result_history = result_history.filter(exam_type=exam_type)

    # Pass the filtered result history and student to the template
    context = {
        'student': student,
        'result_history': result_history,
        'selected_exam_type': exam_type,  # Pass the selected exam type to pre-select the dropdown
    }

    return render(request, 'students_result/result_history.html', context)

