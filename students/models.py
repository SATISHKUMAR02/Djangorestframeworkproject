from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=50)
    student_name = models.CharField(max_length=50)
    student_email = models.CharField(max_length=50)
    student_branch = models.CharField(max_length=50)
    
    def __str__(self):
        return self.student_name

class Teachers(models.Model):
    teacher_id = models.IntegerField()
    teacher_name = models.CharField(max_length=200)
    teacher_email = models.EmailField(max_length=100)
    teacher_branch = models.CharField(max_length=100)

    def __str__(self):
        return self.teacher_name

    
    