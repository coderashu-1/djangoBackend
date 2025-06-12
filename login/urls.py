from django.urls import path
from .views import LoginAuth

urlpatterns = [
    path('login/', LoginAuth.as_view(), name='login-auth'),
]
