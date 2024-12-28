from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Appointment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

class Payment(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50, choices=[
        ('cash', 'Cash to Cash Face to Face'),
        ('gcash', 'Gcash Payment'),
    ])

class Feedback(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    feedback = models.TextField()
    rating = models.PositiveIntegerField(default=5)
