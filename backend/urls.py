from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'backend'

urlpatterns = [
    path('', views.home, name='index'),
    path('shop', views.shop, name='shop'),
    path('shopping_cart', views.shopping_cart, name='shopping_cart'),
    path('checkout', views.checkout, name='checkout'),
    path('updateItem', views.updateItem, name='updateItem'),
    path('404', views.service, name='404'),
    path('register', views.register, name='register'),
    path('thankyou', views.thank_you, name='thankyou'),
    path('login', views.customer_login, name='login'),
    path('logout', views.logout_view , name='logout'),
    
    
]