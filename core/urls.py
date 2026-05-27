
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views  # 1. Импортируем готовые вьюхи авторизации
from clinic.views import main_page, service_detail, doctors_list, doctors_detail, register_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page,name='index'),
    path('service/<int:pk>', service_detail, name='service_detail'),
    path('doctors/', doctors_list, name='doctors_list'),
# Новый динамический путь для одного врача (принимаем его ID):
    path('doctors/<int:pk>', doctors_detail, name='doctor_detail'),
# 2. Новый маршрут для входа:
    # Мы говорим LoginView использовать наш кастомный HTML-шаблон
    path('login/', auth_views.LoginView.as_view(template_name='clinic/login.html'), name='login'),
# Новый маршрут для выхода:
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
# Новый путь для регистрации:
    path('register/', register_view, name='register'),

]
