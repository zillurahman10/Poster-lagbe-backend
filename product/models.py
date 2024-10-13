from typing import Any
from django.db import models

# Create your models here.
status = (
    ('in stock', 'in stock'),
    ('stock out', 'stock out'),
)

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.CharField(max_length=200)
    stock_status = models.CharField(max_length=50, choices=status)
    paper_weight = models.CharField(max_length=50, default="300 gsm")
    paper_type = models.CharField(max_length=50, default="Glossy")
    

    def __str__(self):
        return self.name