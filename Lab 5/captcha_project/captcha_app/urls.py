from django.urls import path
from .views import captcha_view, verify_captcha

urlpatterns = [
    path('', captcha_view, name='captcha'),
    path('verify/', verify_captcha, name='verify_captcha'),
]
