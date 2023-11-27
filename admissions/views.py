from django.shortcuts import render, redirect, get_object_or_404
from .forms import AdmissionForm
from .models import Admission
from .forms import AdmissionYearFilterForm, AdmissionClassFilterForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import StudentUpdateForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse


@login_required
def admission_form(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            
            admission_class = form.cleaned_data['admission_class']
            form.instance.current_class = admission_class
        
            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                print(f'Uploaded file name: {photo.name}')
            else:
                print("No photo attached in the form.")
            
            admission = form.save()
            return redirect('student_details', student_id=admission.id)
        else:
            print(form.errors)
    else:
        form = AdmissionForm()
    return render(request, 'admissions/admission_form.html', {'form': form})

@login_required
def student_list(request):
    students = Admission.objects.all()
    # Apply filters if provided in the GET request
    year_filter_form = AdmissionYearFilterForm(request.POST)
    if year_filter_form.is_valid():
        admission_year = year_filter_form.cleaned_data.get('admission_year')
        if admission_year:
            students = students.filter(admission_date__year=admission_year)

    class_filter_form = AdmissionClassFilterForm(request.POST)
    if class_filter_form.is_valid():
        admission_class = class_filter_form.cleaned_data.get('admission_class')
        if admission_class:
            students = students.filter(admission_class__icontains=admission_class)

    # Paginate the student list
    page = request.GET.get('page')
    paginator = Paginator(students, 20)  # Display 10 students per page, you can adjust this number as needed

    students = paginator.get_page(page)

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

    # Apply filters if provided in the GET request
    year_filter_form = AdmissionYearFilterForm(request.GET)
    if year_filter_form.is_valid():
        admission_year = year_filter_form.cleaned_data.get('admission_year')
        if admission_year:
            class_6_students = class_6_students.filter(admission_date__year=admission_year)

    # Paginate the class 6 student list
    page = request.GET.get('page')
    paginator = Paginator(class_6_students, 20)  # Display 10 students per page, you can adjust this number as needed

    class_6_students = paginator.get_page(page)

    context = {
        'class_6_students': class_6_students,
        'year_filter_form': year_filter_form,
    }

    return render(request, 'admissions/class_6.html', context)


@login_required
def class_7(request):
    class_7_students = Admission.objects.filter(admission_class='7')

    # Apply filters if provided in the GET request
    year_filter_form = AdmissionYearFilterForm(request.GET)
    if year_filter_form.is_valid():
        admission_year = year_filter_form.cleaned_data.get('admission_year')
        if admission_year:
            class_7_students = class_7_students.filter(admission_date__year=admission_year)

    # Paginate the class 7 student list
    page = request.GET.get('page')
    paginator = Paginator(class_7_students, 20)  # Display 10 students per page, you can adjust this number as needed

    class_7_students = paginator.get_page(page)

    context = {
        'class_7_students': class_7_students,
        'year_filter_form': year_filter_form,
    }

    return render(request, 'admissions/class_7.html', context)


@login_required
def class_8(request):
    class_8_students = Admission.objects.filter(admission_class='8')

    # Apply filters if provided in the GET request
    year_filter_form = AdmissionYearFilterForm(request.GET)
    if year_filter_form.is_valid():
        admission_year = year_filter_form.cleaned_data.get('admission_year')
        if admission_year:
            class_8_students = class_8_students.filter(admission_date__year=admission_year)

    # Paginate the class 8 student list
    page = request.GET.get('page')
    paginator = Paginator(class_8_students, 20)  # Display 10 students per page, you can adjust this number as needed

    class_8_students = paginator.get_page(page)

    context = {
        'class_8_students': class_8_students,
        'year_filter_form': year_filter_form,
    }

    return render(request, 'admissions/class_8.html', context)


@login_required
def class_9(request):
    class_9_students = Admission.objects.filter(admission_class='9')

    # Apply filters if provided in the GET request
    year_filter_form = AdmissionYearFilterForm(request.GET)
    if year_filter_form.is_valid():
        admission_year = year_filter_form.cleaned_data.get('admission_year')
        if admission_year:
            class_9_students = class_9_students.filter(admission_date__year=admission_year)

    # Paginate the class 9 student list
    page = request.GET.get('page')
    paginator = Paginator(class_9_students, 20)  # Display 10 students per page, you can adjust this number as needed

    class_9_students = paginator.get_page(page)

    context = {
        'class_9_students': class_9_students,
        'year_filter_form': year_filter_form,
    }

    return render(request, 'admissions/class_9.html', context)



@login_required
def class_10(request):
    class_10_students = Admission.objects.filter(admission_class='10')

    # Apply filters if provided in the GET request
    year_filter_form = AdmissionYearFilterForm(request.GET)
    if year_filter_form.is_valid():
        admission_year = year_filter_form.cleaned_data.get('admission_year')
        if admission_year:
            class_10_students = class_10_students.filter(admission_date__year=admission_year)

    # Paginate the class 10 student list
    page = request.GET.get('page')
    paginator = Paginator(class_10_students, 20)  # Display 10 students per page, you can adjust this number as needed

    class_10_students = paginator.get_page(page)

    context = {
        'class_10_students': class_10_students,
        'year_filter_form': year_filter_form,
    }

    return render(request, 'admissions/class_10.html', context)


@login_required
def class_11(request):
    class_11_students = Admission.objects.filter(admission_class='11')

    # Apply filters if provided in the GET request
    year_filter_form = AdmissionYearFilterForm(request.GET)
    if year_filter_form.is_valid():
        admission_year = year_filter_form.cleaned_data.get('admission_year')
        if admission_year:
            class_11_students = class_11_students.filter(admission_date__year=admission_year)

    # Paginate the class 11 student list
    page = request.GET.get('page')
    paginator = Paginator(class_11_students, 20)  # Display 10 students per page, you can adjust this number as needed

    class_11_students = paginator.get_page(page)

    context = {
        'class_11_students': class_11_students,
        'year_filter_form': year_filter_form,
    }

    return render(request, 'admissions/class_11.html', context)


@login_required
def class_12(request):
    class_12_students = Admission.objects.filter(admission_class='12')

    # Apply filters if provided in the GET request
    year_filter_form = AdmissionYearFilterForm(request.GET)
    if year_filter_form.is_valid():
        admission_year = year_filter_form.cleaned_data.get('admission_year')
        if admission_year:
            class_12_students = class_12_students.filter(admission_date__year=admission_year)

    # Paginate the class 12 student list
    page = request.GET.get('page')
    paginator = Paginator(class_12_students, 20)  # Display 10 students per page, you can adjust this number as needed

    class_12_students = paginator.get_page(page)

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
            'current_class': student.current_class,
        }
        for student in students
    ]
    
    # Return the JSON response
    return JsonResponse(student_data, safe=False)

@login_required
def update_student(request, student_id):
    student = get_object_or_404(Admission, id=student_id)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, request.FILES, instance=student)  # Include request.FILES
        if form.is_valid():
            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                print(f'Uploaded file name: {photo.name}')
            else:
                print("No photo attached in the form.")
            form.save()
            return redirect('student_list')  # Redirect back to the student list page
        else:
            print(form.errors)
    else:
        form = StudentUpdateForm(instance=student)

    context = {
        'student': student,
        'form': form,
    }

    return render(request, 'admissions/update_student.html', context)
    

@login_required
def update_student_class_6(request, student_id):
    student = get_object_or_404(Admission, id=student_id)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                print(f'Uploaded file name: {photo.name}')
            else:
                print("No photo attached in the form.")
            form.save()
            return redirect('class_6')  # Redirect back to the class 6 page
    else:
        form = StudentUpdateForm(instance=student)

    context = {
        'student': student,
        'form': form,
    }

    return render(request, 'admissions/update_student.html', context)

@login_required
def update_student_class_7(request, student_id):
    student = get_object_or_404(Admission, id=student_id)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                print(f'Uploaded file name: {photo.name}')
            else:
                print("No photo attached in the form.")
            form.save()
            return redirect('class_7')  # Redirect back to the class 6 page
    else:
        form = StudentUpdateForm(instance=student)

    context = {
        'student': student,
        'form': form,
    }

    return render(request, 'admissions/update_student.html', context)

@login_required
def update_student_class_8(request, student_id):
    student = get_object_or_404(Admission, id=student_id)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                print(f'Uploaded file name: {photo.name}')
            else:
                print("No photo attached in the form.")
            form.save()
            return redirect('class_8')  # Redirect back to the class 6 page
    else:
        form = StudentUpdateForm(instance=student)

    context = {
        'student': student,
        'form': form,
    }

    return render(request, 'admissions/update_student.html', context)

@login_required
def update_student_class_9(request, student_id):
    student = get_object_or_404(Admission, id=student_id)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                print(f'Uploaded file name: {photo.name}')
            else:
                print("No photo attached in the form.")
            form.save()
            return redirect('class_9')  # Redirect back to the class 6 page
    else:
        form = StudentUpdateForm(instance=student)

    context = {
        'student': student,
        'form': form,
    }

    return render(request, 'admissions/update_student.html', context)

@login_required
def update_student_class_10(request, student_id):
    student = get_object_or_404(Admission, id=student_id)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                print(f'Uploaded file name: {photo.name}')
            else:
                print("No photo attached in the form.")
            form.save()
            return redirect('class_10')  # Redirect back to the class 6 page
    else:
        form = StudentUpdateForm(instance=student)

    context = {
        'student': student,
        'form': form,
    }

    return render(request, 'admissions/update_student.html', context)

@login_required
def update_student_class_11(request, student_id):
    student = get_object_or_404(Admission, id=student_id)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, request.FILES,  instance=student)
        if form.is_valid():
            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                print(f'Uploaded file name: {photo.name}')
            else:
                print("No photo attached in the form.")
            form.save()
            return redirect('class_11')  # Redirect back to the class 6 page
    else:
        form = StudentUpdateForm(instance=student)

    context = {
        'student': student,
        'form': form,
    }

    return render(request, 'admissions/update_student.html', context)

@login_required
def update_student_class_12(request, student_id):
    student = get_object_or_404(Admission, id=student_id)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                print(f'Uploaded file name: {photo.name}')
            else:
                print("No photo attached in the form.")
            form.save()
            return redirect('class_12')  # Redirect back to the class 6 page
    else:
        form = StudentUpdateForm(instance=student)

    context = {
        'student': student,
        'form': form, 
    }

    return render(request, 'admissions/update_student.html', context)

def get_user_count(request):
    # Retrieve the user count from the User model
    user_count = User.objects.count()
    
    # Create a JSON response with the user count
    response_data = {'total_users': user_count}
    return JsonResponse(response_data)

@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Admission, id=student_id)
    student.delete()
    messages.success(request, 'Student deleted successfully.')
    return HttpResponseRedirect(reverse('student_list')) 