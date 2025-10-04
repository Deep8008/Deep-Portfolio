from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def home_view(request):
    return render(request, "main_pages/index.html")

def support_view(request):
    return render(request, "main_pages/support.html")

def about_view(request):
    return render(request, "main_pages/about.html")
