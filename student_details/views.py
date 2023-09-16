# student_details/views.py
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Student
import datetime
from .forms import StudentSearchForm

def student_list(request):
    current_year = datetime.datetime.now().year
    students = Student.objects.filter(current_year=current_year)
    # Retrieve all students with their associated admission information
    students = Student.objects.all()
    
    # Pagination
    paginator = Paginator(students, 20)  # Display 20 students per page
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    return render(request, 'student_details/student_list.html', {'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_details/student_detail.html', {'student': student})


# student_details/views.py
def student_search(request):
    if request.method == 'POST':
        form = StudentSearchForm(request.POST)
        if form.is_valid():
            current_year = form.cleaned_data['current_year']
            students = Student.objects.filter(current_year=current_year)
            return render(request, 'student_details/student_list.html', {'students': students})
    else:
        form = StudentSearchForm()
    return render(request, 'student_details/student_search.html', {'form': form})
