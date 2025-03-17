from django.urls import path
from .views import billing_form, process_bill

urlpatterns = [
    path('', billing_form, name='billing_form'),
    path('process_bill/', process_bill, name='process_bill'),
]
