from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def main_page(request):
    return render(request, 'clinic/index.html')
