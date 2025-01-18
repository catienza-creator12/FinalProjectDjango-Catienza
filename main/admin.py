from django.contrib import admin
from .models import Customer, Service, Appointment, Payment, Feedback

admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Payment)
admin.site.register(Feedback)

class CustomAdminSite(admin.AdminSite):
    def login(self, request, extra_context=None):
        if request.user.is_authenticated:
            Customer.objects.get_or_create(user=request.user)
        return super().login(request, extra_context)

admin_site = CustomAdminSite(name='myadmin')
