from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def aboutus(request):
    return render(request, 'aboutus.html')