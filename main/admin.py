from django.contrib import admin
from .models import Customer, Service, Appointment, Payment, Feedback

admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Payment)
admin.site.register(Feedback)
