from django.urls import path
from . import views

urlpatterns = [
    path('fee/', views.fee_detail, name='fee_detail'),
    #path('add_fee/', views.add_fee, name='add_fee'),
    path('fee_detail/', views.fee_detail, name='fee_detail'),
    path('fee_submission/<int:student_id>/', views.fee_submission, name='fee_submission'),
]