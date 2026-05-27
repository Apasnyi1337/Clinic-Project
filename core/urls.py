
from django.contrib import admin
from django.urls import path
from clinic.views import main_page, service_detail, doctors_list, doctors_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page,name='index'),
    path('service/<int:pk>', service_detail, name='service_detail'),
    path('doctors/', doctors_list, name='doctors_list'),
# Новый динамический путь для одного врача (принимаем его ID):
    path('doctors/<int:pk>', doctors_detail, name='doctor_detail'),
]
