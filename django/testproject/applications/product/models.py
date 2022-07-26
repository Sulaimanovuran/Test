from django.db import models


class Product(models.Model):
    title = models.CharField("Название", max_length=50)
    price = models.BigIntegerField("Цена")

    class Meta:
        ordering = ['id']
        verbose_name ='Продукт'
        verbose_name_plural ='Продукты'

    def __str__(self):
        return f'{self.id} - {self.title}'