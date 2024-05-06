from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import uuid


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, null=True)
    def __str__(self) -> str:
        return self.username
    
    
class Products(models.Model):
    ProductName = models.CharField(max_length=255)
    Description = models.TextField(max_length=1000)
    Price = models.FloatField()
    QauntityInStock = models.IntegerField()
    image = CloudinaryField('image')
    
    def __str__(self) -> str:
        return self.ProductName
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    
        
    
    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product.ProductName
    
    @property
    def get_total(self):
        total = self.product.Price * self.quantity
        return total