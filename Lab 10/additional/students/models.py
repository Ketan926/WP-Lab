from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.student_name} - {self.course_name}"