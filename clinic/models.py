from django.db import models

# Create your models here.
from django.db import models
class Service(models.Model):
    # 1. Название услуги. Переменная строка с ограничением в 100 символов.
    title = models.CharField(max_length=100, verbose_name='Название услуги')
    # 2. Описание услуги. Текстовое поле для большого количества текста.
    description = models.TextField(verbose_name="Описание услуги", blank=True)
    # 3. Стоимость. Целое число.
    price = models.PositiveIntegerField(verbose_name="Стоймость (руб.)")
    # Этот метод нужен, чтобы в админке Django красиво отображалось имя объекта, а не надпись "Service object (1)"
    def __str__(self):
        return self.title


class Doctor(models.Model):
    # 1. ФИО врача
    full_name = models.CharField(max_length=100, verbose_name="ФИО врача")

    # 2. Специализация (например: Хирург, Терапевт, Стоматолог)
    specialty = models.CharField(max_length=100, verbose_name="Специализация")

    # 3. Стаж работы (в годах)
    experience = models.PositiveIntegerField(verbose_name="Стаж (лет)")

    def __str__(self):
        return f"{self.full_name} ({self.specialty})"


class Appointment(models.Model):
    client_name = models.CharField(max_length=100, verbose_name="Имя владельца")

    pet_name = models.CharField(max_length=100, verbose_name="Кличка питомца")

    phone = models.CharField(max_length=20, verbose_name="Номер телефона")

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        verbose_name="Какая услуга требуется"
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Желаемый врач"

    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявка")

    def __str__(self):
        return f"Запись: {self.pet_name} ({self.client_name}) - {self.phone}"

