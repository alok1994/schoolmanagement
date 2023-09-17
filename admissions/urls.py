# admissions/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('admission/', views.admission_form, name='admission_form'),
    path('student_list/', views.student_list, name='student_list'),
    path('student/<int:student_id>/', views.student_details, name='student_details')
]
