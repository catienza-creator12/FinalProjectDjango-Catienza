from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Service

class ServiceListView(ListView):
    model = Service
    template_name = 'service/list.html'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service/detail.html'

class ServiceCreateView(CreateView):
    model = Service
    fields = ['name', 'description']
    template_name = 'service/form.html'
    success_url = reverse_lazy('service-list')

class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['name', 'description']
    template_name = 'service/form.html'
    success_url = reverse_lazy('service-list')

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'service/confirm_delete.html'
    success_url = reverse_lazy('service-list')
