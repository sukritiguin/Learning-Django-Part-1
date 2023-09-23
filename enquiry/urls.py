# enquiry/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('enquiry/', views.enquiry_form, name='enquiry_form'),
    path('enquiry/success/', views.enquiry_success, name='enquiry_success'),
]
