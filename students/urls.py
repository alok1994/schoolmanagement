from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.student_list, name='student_list'),
    #path('login/', views.CustomLoginView.as_view(), name='custom_login'),
    path('login/', views.custom_login, name='custom_login'),
    path('logout/', views.logout_view, name='logout'),
]
