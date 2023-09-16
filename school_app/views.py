from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_views(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the dashboard or any other desired page upon successful login
            print('Login Successfull')
            return redirect('dashboard')  # 'dashboard' should be replaced with the actual name of your dashboard URL pattern
        else:
            # Handle authentication failure (e.g., display an error message)
            pass  # You can add error handling here

    return render(request, 'registration/login.html')


@login_required
def dashboard_view(request):
    # Add logic to display the dashboard here
    return render(request, 'registration/dashboard.html')