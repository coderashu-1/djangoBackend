from django.urls import path
from .views import ExportRegisterForm, ExportRegisterView

urlpatterns = [
    path('form/', ExportRegisterForm.as_view(), name='exportregister-form'),
    path('view/', ExportRegisterView.as_view(), name='exportregister-view'),
]
