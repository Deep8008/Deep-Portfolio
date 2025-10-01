from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to the Home page!</h1>")

def support_view(request):
    return HttpResponse("<h1>Support page</h1>")

def about_view(request):
    return HttpResponse("<h1>About page</h1>")
