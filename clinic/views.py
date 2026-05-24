from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def main_page(request):
    return HttpResponse("<h1>Привет! Это главная страница нашей ветклиники!</h1>")
