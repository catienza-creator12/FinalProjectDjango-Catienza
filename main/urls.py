from django.urls import path
from .views import (
    ServiceListView, ServiceDetailView, ServiceCreateView, 
    ServiceUpdateView, ServiceDeleteView,
)

urlpatterns = [
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('services/create/', ServiceCreateView.as_view(), name='service-create'),
    path('services/<int:pk>/update/', ServiceUpdateView.as_view(), name='service-update'),
    path('services/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service-delete'),
]
