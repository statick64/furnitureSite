from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect 
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponse
import json

from .forms import SignUpForm, UserCreationForm
from .models import Products, Customer, Order
# Create your views here.
def home(request):
    return render(request, "index.html")

def shop(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, "shop.html", context=context)

def shopping_cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    
    else:
        items = []
    context = {'items':items}
    
    return render(request, "cart.html", context=context)

@csrf_protect
def login_signup(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid:
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                form.save()
                new_user = authenticate(username=username, password=password)
                if new_user is not None:
                    login(request, new_user)
                    # return redirect('home')           
    else:
        pass
        # return redirect('home')
    
    form = SignUpForm()
    context = {"form":form}
    return render(request, "login_singup.html", context=context)

def shopping_cart(request):
    return render(request, "cart.html")