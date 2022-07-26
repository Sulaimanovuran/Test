from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Product(models.Model):
    MANUFACTURER = (
        ('KG', 'Кыргызстан'),
        ('USA', 'США'),
        ('KR', 'Корея'),
        ('UK', 'Украина'),
        ('RU', 'Россия'),
        ('JP', 'Япония'),
        ('CN', 'Китай')
    )
    name = models.CharField(max_lenght=50)
    cost = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    made_in = models.CharField(max_length=30, choices=MANUFACTURER)
    create_date = models.DateField(auto_created=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')


