from rest_framework import serializers
from students.models import *
from employees.models import *



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__" # indicating all the fields in model to be serialized

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

