from django.db import models

# Create your models here.
class Student(models.Model):
    student_name=models.TextField()
    student_age =models.IntegerField()
    address     =models.CharField(max_length=20)

class Employee(models.Model):
    employee_name= models.CharField(max_length=50)
    employee_address= models.TextField()
    employee_phone=models.IntegerField()
# Employee employee_name, employee_address, employee_phone
