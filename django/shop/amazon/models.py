from django.db import models

class Catalogs(models.Model):
    name = models.SlugField(primary_key=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    MANUFACTURER = (
        ('USA', 'United States'),
        ('EN', 'English'),
        ('KG', 'Kyrgyzstan'),
        ('KZ', 'Kazakhstan'),
        ('UZ', 'Uzbekstan'),
        ('CN', 'China'),
        ('KR', 'Korea')
    )
    name = models.CharField(max_length=50)
    cost = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    production_date = models.DateField(auto_now_add=True)
    made_in = models.CharField(max_length=50, choices=MANUFACTURER)
    catalog = models.ForeignKey(Catalogs, on_delete=models.CASCADE, related_name='products')

    def __str__(self) -> str:
        return f'{self.name}|    |{self.catalog}|    |{self.made_in}'


