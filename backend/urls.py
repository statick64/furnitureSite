from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'backend'

urlpatterns = [
    path('', views.home, name='index'),
    path('shop', views.shop, name='shop'),
    path('shopping_cart', views.shopping_cart, name='shopping_cart'),
    path('login_signup', views.login_or_register, name='login_signup'),
    path('404', views.service, name='404'),
    path('register', views.register, name='register'),
    path('login', views.customer_login, name='login'),
    
    
]