from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Service, Appointment, Doctor  # Импортируем нашу модель (точка означает "из текущей папки")

# Регистрируем модель Service в админке
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Doctor)
