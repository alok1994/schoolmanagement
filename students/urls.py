from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.student_list, name='student_list'),
]
