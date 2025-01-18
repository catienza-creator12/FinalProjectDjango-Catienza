from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True, default='services/default_service.png')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

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

@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_customer_profile(sender, instance, **kwargs):
    instance.customer.save()

def get_customer(user):
    return Customer.objects.get_or_create(user=user)[0]

User.add_to_class('customer', property(get_customer))
