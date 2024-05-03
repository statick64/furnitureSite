from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json



# Create your views here.
def home(request):
    return render(request, "index.html")

def shop(request):
    return render(request, "shop.html")

def login_signup(request):
    return render(request, "login_singup.html")