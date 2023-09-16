# admission_form/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('admission/', views.admission_form, name='admission_form'),
]
