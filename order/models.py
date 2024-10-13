from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
status = (
    ('Pending', 'Pending'),
    ('Confirmed', 'Confirmed'),
    ('Pending', 'Pending'),
)

class Order(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=300)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()    
    created_at = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=100, choices=status)