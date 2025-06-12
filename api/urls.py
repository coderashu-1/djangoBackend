from django.urls import path
from .views import AdminDashboard

urlpatterns = [
    path('adminDashboard/', AdminDashboard.as_view(), name='admin-dashboard'),
]
