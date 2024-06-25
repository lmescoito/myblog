from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(requets):
    return HttpResponse("Welcome to the Blog Home Page")

def admin_view(request):
    return render (request, 'admin_page.html')