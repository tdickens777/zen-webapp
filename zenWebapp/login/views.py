from django.shortcuts import render

def index(request):
    return render(request, 'login/index.html')

def register(request):
    return render(request, 'login/register.html')