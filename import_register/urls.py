from django.urls import path
from .views import ImportRegisterForm, ImportRegisterView

urlpatterns = [
    path('form/', ImportRegisterForm.as_view(), name='importregister-form'),
    path('view/', ImportRegisterView.as_view(), name='importregister-view'),
]

