from django.urls import path
from students_result import views

urlpatterns = [
    path('students_result/', views.students_result, name='students_result'),
    path('create_result/<int:student_id>/', views.create_result, name='create_result'),
    path('result_history/<int:student_id>/', views.result_history, name='result_history'),
]
