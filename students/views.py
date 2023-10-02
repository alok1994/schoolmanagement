from django.shortcuts import render,redirect 
from .models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.contrib import messages


@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})


def logout_view(request):
    # Perform logout logic here
    logout(request)
    # Redirect to the logout success page or render a template
    return render(request, 'students/logout.html')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to your dashboard or another page
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')

    return render(request, 'students/login.html')