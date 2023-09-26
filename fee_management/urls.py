from django.urls import path
from . import views

urlpatterns = [
    path('fee/', views.fee_detail, name='fee_detail'),
    #path('add_fee/', views.add_fee, name='add_fee'),
    path('fee_detail/', views.fee_detail, name='fee_detail'),
    path('fee_submission/<int:student_id>/', views.fee_submission, name='fee_submission'),
    path('fee_history/<int:student_id>/', views.fee_history, name='fee_history'),
    path('generate_receipt/<int:fee_id>/', views.generate_receipt, name='generate_receipt'),
    
]