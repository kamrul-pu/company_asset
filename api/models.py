from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Device(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    condition_choices = (
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor')
    )
    condition = models.CharField(max_length=10, choices=condition_choices)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checked_out = models.DateTimeField()
    checked_in = models.DateTimeField(null=True, blank=True)
    condition_choices = (
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor')
    )
    condition = models.CharField(max_length=10, choices=condition_choices)

    def __str__(self):
        return f"{self.device} checked out by {self.employee} on {self.checked_out}"
