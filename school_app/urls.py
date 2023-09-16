# school_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard')
]
