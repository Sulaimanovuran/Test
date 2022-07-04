from models import Product,Category

def add_category(name):
    try:
        row = Category(name=name)
        row.save()
        print('saved')
    except:
        print("Такая категория уже существует")

def add_product(name, price, category):
    category_id = Category.select().where(Category.name==category)
    row = Product(name = name, price = price, category = category_id)
    row.save()


# add_category('Game')

# add_product(name='Teddy',price = 4500 ,category = 'Game')


def get_categories():
    categories = Category.select()
    # print(categories)
    for i in categories:
        print(i.id,end=' ')
        print(i.name)

# get_categories()


def get_products():
    products = Product.select()
    for i in products:
        print(f'{i.name} {i.price} {i.category.name}')

# get_products()


def delete_product(id):
    product = Product.select().where(Product.id == id)
    product[0].delete_instance()

# delete_product(2)

def update_product(id, name):
    product = Product.get(Product.id == id)
    product.name = name
    product.save()
    #(Product.update(name=name).where(Product.id==id)).execute()