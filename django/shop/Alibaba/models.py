from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Product(models.Model):
    Made_in = (
        ('KG', 'Кыргызстан'),
        ('KR', 'Корея'),
        ('USA', 'США')
    )
    manufacturer = models.ManyToManyField(User)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name= 'product')
    created_at = models.DateField(auto_now_add=True)
    country = models.CharField(max_length=30, choices=Made_in)
    def __str__(self):
        return f'{self.name} |    | {self.category}'