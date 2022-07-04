import peewee
from settings import db


class Category(peewee.Model):
    id = peewee.PrimaryKeyField(null=False)
    name = peewee.CharField(max_length=100, unique=True)

    class Meta:
        database = db
        db_table = 'categories'


# Category.create_table()

class Product(peewee.Model):
    id = peewee.PrimaryKeyField(null=False)
    name = peewee.CharField(max_length=50)
    price = peewee.DecimalField(max_digits=10, decimal_places=2, default=10)
    category = peewee.ForeignKeyField(Category, related_name = 'products', to_field = 'id', on_delete='cascade')

    class Meta:
        database = db
        db_table = 'products'

# Product.create_table()
