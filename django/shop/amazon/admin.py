from django.contrib import admin
from amazon.models import Catalogs, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost', 'production_date', 'catalog']
    list_filter = ['catalog']
    search_fields = ['id']


admin.site.register(Catalogs)
admin.site.register(Product, ProductAdmin)