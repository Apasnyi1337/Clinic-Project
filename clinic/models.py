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