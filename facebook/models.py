from django.db import models


class Employee(models.Model):
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    name = models.CharField(max_length=300, null=True)
    age = models.IntegerField(null=True)


class EmployeesFriend(models.Model):
    employee = models.ForeignKey(Employee, models.CASCADE)
    name = models.CharField(max_length=300)
    birthday = models.DateField(null=True)
