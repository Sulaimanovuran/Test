from django.db import models


class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    full_name = models.CharField(max_length=50)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name} - {self.create_date}'
