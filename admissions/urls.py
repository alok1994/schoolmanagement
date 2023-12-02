# admissions/urls.py
from django.urls import path
from . import views
from .views import get_weekly_admissions

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
    path('class_12/', views.class_12, name='class_12'),
    path('api/students/', views.get_student_data, name='get_student_data'),
    path('update_student/<int:student_id>/', views.update_student, name='update_student'),
    path('class-6/update/<int:student_id>/', views.update_student_class_6, name='update_student_class_6'),
    path('class-7/update/<int:student_id>/', views.update_student_class_7, name='update_student_class_7'),
    path('class-8/update/<int:student_id>/', views.update_student_class_8, name='update_student_class_8'),
    path('class-9/update/<int:student_id>/', views.update_student_class_9, name='update_student_class_9'),
    path('class-10/update/<int:student_id>/', views.update_student_class_10, name='update_student_class_10'),
    path('class-11/update/<int:student_id>/', views.update_student_class_11, name='update_student_class_11'),
    path('class-12/update/<int:student_id>/', views.update_student_class_12, name='update_student_class_12'),
    path('api/user-count/', views.get_user_count, name='user_count_api'),
    path('student-list/delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('api/weekly-admissions/', get_weekly_admissions, name='weekly_admissions'),


]
