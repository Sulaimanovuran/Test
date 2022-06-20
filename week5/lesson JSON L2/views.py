FILE_PATH = 'data.json'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)

def get_one_data():
    data = get_data()
    id = int(input("Введите id продукта: "))
    element = list(filter(lambda x: x['id'] == id, data))
    return element[0]

def post_data():
    data = get_data()
    data.append({
        'id': random.randint(1,10000000),
        'name': input('Введите название продукта: '),
        'price': float(input('Введите цену на продукт'))

    })
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
        return 'Created'


def update_data():
    data = get_data()
    id = int(input('Введите id продукта: '))
    update = list(filter(lambda x: x['id'] == id, data))
    if not update:
        return "Нет такого подукта"
      
    index = data.index(update[0])
    data[index]['name'] = input('Введите новое название: ')
    data[index]['price'] = float(input())
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    return 'updated'
import json
import random

def delete_data():
    data = get_data()
    id = int(input('Введите id прдукта: '))
    delete = list(filter(lambda x: x['id'] == id, data))
    if not delete:
        return 'Нет такого продукта'

    index = data.index(delete[0])
    data.pop(index)

    json.dump(data, open(FILE_PATH, 'w'))

    return 'deleted'
delete_data()