from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect 
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse


from .forms import SignUpForm, UserCreationForm, CustomAuthenticationForm
from .models import Products, Customer, Order
# Create your views here.
def home(request):
    return render(request, "index.html")

def service(request):
    return render(request, "services.html")

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('backend:login')  # Redirect to home page after successful registration
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


def shop(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, "shop.html", context=context)

from .models import OrderItem

@login_required
def shopping_cart(request):
    try:
        order = request.user.customer.order_set.get(complete=False)
        items = order.orderitem_set.all()
        print(items)
    except Order.DoesNotExist:
        order = None
        items = []

    context = {'items': items}
    return render(request, "cart.html", context=context)



# def login_signup(request):
#     if request.user.is_anonymous:
#         if request.method == "POST":
#             form = SignUpForm(request.POST)
#             if form.is_valid:
#                 username = form.cleaned_data.get('username')
#                 password = form.cleaned_data.get('password1')
#                 form.save()
#                 new_user = authenticate(username=username, password=password)
#                 if new_user is not None:
#                     login(request, new_user)
#                     # return redirect('home')           
#     else:
#         pass
#         # return redirect('home')
    
#     form = SignUpForm()
#     context = {"form":form}
#     return render(request, "login_singup.html", context=context)

@csrf_protect
def login_or_register(request):
    if request.method == 'POST':
        # Check if the form submitted is for registration or login
        if 'register' in request.POST:
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('404')  # Redirect to home page after successful registration
        elif 'login' in request.POST:
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('404')  # Redirect to home page after successful login
    else:
        form = SignUpForm()  # Assuming register form is displayed initially
    return render(request, 'login_singup.html', {'form': form})


