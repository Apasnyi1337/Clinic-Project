from django import forms
from .models import Appointment
class AppointmentForm(forms.ModelForm):
    class Meta:
        # 1. Говорим Django, на основе какой модели строить форму
        model = Appointment
        # 2. Указываем, какие поля из этой модели должен заполнять пользователь.
        # Дату (created_at) мы не берем, она заполнится сама автоматически.
        fields = ['client_name', 'pet_name', 'phone', 'service', 'doctor']

    # Специальная функция для валидации поля phone
    def clean_phone(self):
        # Достаем то, что пользователь ввел в поле телефона
        phone = str(self.cleaned_data.get('phone', ''))
        # Удаляем ВООБЩЕ ВСЕ пробелы, дефисы и скобки, которые мог ввести пользователь
        for char in [" ", "-", "(", ")"]:
            phone = phone.replace(char, "")
        # 1. Удаляем пробелы по краям, если пользователь случайно их поставил
        phone = phone.strip()
        # 2. Проверяем длину (например, российский номер с +7 — это 12 символов, без + — 11)
        if len(phone) < 11 or len(phone) > 15:
            raise forms.ValidationError('Номер телефона должен содержать от 11 до 15 символов!')
# 3. Проверяем, что в номере нет букв.
        # Разрешаем только цифры, ну и знак "+" в самом начале, если он есть
        allowed_chars = set("0123456789+")
        for char in phone:
            if char not in allowed_chars:
                raise forms.ValidationError('"Номер телефона может содержать только цифры и знак + !')
            
        return phone
