from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
import json


from .forms import SignUpForm, UserCreationForm, CustomAuthenticationForm
from .models import Products, Customer, Order, OrderItem
# Create your views here.
def home(request):
    return render(request, "index.html")

def service(request):
    return render(request, "services.html")

def thank_you(request):
    return render(request, "thankyou.html")

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('backend:thankyou')  # Redirect to home page after successful registration
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

@csrf_protect
def customer_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('backend:index')  # Redirect to home page after successful login
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('backend:index')
    


def shop(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, "shop.html", context=context)


@login_required
def shopping_cart(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        print(items)
        print(created)
    else:
        order = {'get_cart_total': 0}
        items = []

    context = {'items': items, 'order': order}
    return render(request, "cart.html", context=context)


def checkout(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        print(items)
        print(created)
    else:
        order = {'get_cart_total': 0}
        items = []

    context = {'items': items, 'order': order}
    return render(request, "checkout.html", context=context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)
    
    customer = request.user.customer
    product = Products.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)


