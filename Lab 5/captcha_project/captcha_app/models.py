from django.db import models

# Create your models here.
from django.db import models

class CaptchaAttempt(models.Model):
    session_id = models.CharField(max_length=255, unique=True)
    attempts = models.IntegerField(default=0)
