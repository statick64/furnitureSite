from django.db import models


# Create your models here.


class Products(models.Model):
    ProductName = models.CharField(max_length=255)
    Description = models.TextField(max_length=1000)
    Price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    QauntityInStock = models.IntegerField()
    # image = models.ImageField(upload_to="/images")