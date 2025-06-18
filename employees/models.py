from django.db import models

# Create your models here.
class Employee(models.Model):
    e_id = models.IntegerField()
    e_name = models.CharField(max_length=200)
    e_email = models.EmailField(max_length=100)
    e_branch = models.CharField(max_length=100) 

    def __str__(self):
        return self.e_name