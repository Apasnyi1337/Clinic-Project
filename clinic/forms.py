from django import forms
from .models import Appointment
class AppointmentForm(forms.ModelForm):
    class Meta:
        # 1. Говорим Django, на основе какой модели строить форму
        model = Appointment
        # 2. Указываем, какие поля из этой модели должен заполнять пользователь.
        # Дату (created_at) мы не берем, она заполнится сама автоматически.
        fields = ['client_name', 'pet_name', 'phone', 'service', 'doctor']

