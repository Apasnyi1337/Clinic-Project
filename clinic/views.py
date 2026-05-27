from .forms import AppointmentForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm  # Импортируем встроенную форму регистрации
from django.contrib.auth import login as auth_login    # Импортируем функцию для автоматического входа
# Create your views here.
from django.http import HttpResponse

from clinic.models import Service, Doctor, Appointment
from django.shortcuts import render, redirect

def main_page(request):
    # Проверяем: если пользователь нажал на кнопку отправки формы (метод POST)
    if request.method == 'POST':
        form = AppointmentForm(request.POST) # Набиваем форму данными, которые прислал пользователь
        if form.is_valid(): # Проверяем, всё ли заполнено корректно
            form.save() # МАГИЯ: Django сам создает запись в базе данных!
            return redirect('index') # Перезагружаем страницу, чтобы форма очистилась
   # Если пользователь просто открыл страницу (метод GET), создаем пустую форму
    else:
        form = AppointmentForm()
    # 2. Просим Django забрать вообще все записи об услугах из базы данных.
    # На языке SQL это звучит как: "SELECT * FROM clinic_service;"
    all_services = Service.objects.all()

    # 3. Упаковываем эти услуги в специальный ящик (называется "контекст").
    # Это обычный словарь Python. Нам нужен ключ 'services' — по нему мы будем искать данные внутри HTML.
    # Кладем в наш ящик (контекст) и услуги, и саму форму
    context = {'services': all_services,
               'form': form}
    return render(request, 'clinic/index.html', context)

def service_detail(request, pk):
# pk (Primary Key) — это тот самый ID услуги, который прилетит из URL-адреса.
# Функция get_object_or_404 берет модель и ищет запись с таким pk.
# Если находит — отдает её. Если мы введем несуществующий ID (например, 999),
# она автоматически покажет красивую стандартную ошибку 404 (Страница не найдена).
    service = get_object_or_404(Service, pk=pk)
    context = {'service': service}
    return render(request, 'clinic/detail.html', context)

def doctors_list(request):
    all_doctors = Doctor.objects.all()

    context = {'doctors': all_doctors}
    return render(request, 'clinic/doctors.html', context)

def doctors_detail(request, pk):
    # Находим доктора по ID или выдаем 404
    doctor = get_object_or_404(Doctor, pk=pk)
    # Используем обратную связь, чтобы достать все записи именно этого врача!
    appointments = doctor.appointment_set.all()
    context = {'appointments': appointments, 'doctor': doctor}
    return render(request, 'clinic/doctor_detail.html', context)

def register_view(request):
    # Если пользователь отправил заполненную форму (нажал кнопку "Зарегистрироваться")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
    # Сохраняем нового пользователя в базу данных
            user = form.save()
    # Нам знакома эта магия: автоматически логиним пользователя сразу после регистрации
            auth_login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'clinic/register.html', context)
