# admissions/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('admission/', views.admission_form, name='admission_form'),
    path('student_list/', views.student_list, name='student_list'),
    path('student/<int:student_id>/', views.student_details, name='student_details'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('class_6/', views.class_6, name='class_6'),
    path('class_7/', views.class_7, name='class_7'),
    path('class_8/', views.class_8, name='class_8'),
    path('class_9/', views.class_9, name='class_9'),
    path('class_10/', views.class_10, name='class_10'),
    path('class_11/', views.class_11, name='class_11'),
    path('class_12/', views.class_12, name='class_12')   
]
