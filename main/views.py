from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Service, Feedback, Customer, Appointment
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def homepage_view(request):
    return render(request, 'homepage.html')

@login_required
def appointment_booking_view(request):
    services = Service.objects.all()
    
    if request.method == 'POST':
        customer_phone = request.POST.get('customer_phone')
        service = Service.objects.get(id=request.POST.get('service'))
        date = request.POST.get('date')
        time = request.POST.get('time')

        customer, created = Customer.objects.get_or_create(user=request.user)
        customer.phone = customer_phone
        customer.save()

        Appointment.objects.create(customer=customer, service=service, date=date, time=time)

        return redirect('service-list')

    return render(request, 'appointment/appointment_booking.html', {'services': services})

class CustomLoginView(LoginView):
    template_name = 'customer/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.request.user
        if not hasattr(user, 'customer'):
            Customer.objects.create(user=user)
        return response

class SignUpView(CreateView):
    template_name = 'customer/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['appointment', 'feedback', 'rating']
    template_name = 'feedback/form.html'
    success_url = reverse_lazy('service-list')

class ServiceListView(ListView):
    model = Service
    template_name = 'service/list.html'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service/detail.html'

class ServiceCreateView(CreateView):
    model = Service
    fields = ['name', 'description', 'image', 'price']
    template_name = 'service/form.html'
    success_url = reverse_lazy('service-list')

class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['name', 'description', 'image', 'price']
    template_name = 'service/form.html'
    success_url = reverse_lazy('service-list')

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'service/confirm_delete.html'
    success_url = reverse_lazy('service-list')
