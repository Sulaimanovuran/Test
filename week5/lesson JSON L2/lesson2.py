# CRUD интернет магазина на функциях. Работа с JSON
    # C - create
    # R - read
    # U - update
    # D - delete


# JSON (JavaScript Object Notation) - простой формат обмена данными


# import json
# data = {
#     'name': 'John',
#     'age': 30,
#     'last_name': None,
#     'is_admin': False
# }


# json_obj = json.dumps(data) # Серилизация (перевод данных в json)
# print(json_obj)

# python_obj = json.loads(json_obj) # Десерилизация (перевод с json в python)
# print(python_obj)


### Разница типов данных
#python    json
#dict      object
#list      array
#tuple      array
#str        String
#int        Number
#float      Number
#True,False true/false
#None       null

# import json
# with open('test.json') as file:
#     # print (file.read())
#     print (json.loads(file.read()))



# data = {'is_admin': True}
# print(json.dumps(data))

# with open('test.json') as file:
#     print(json.load(file))


# разница между load и loads, а также dump и dumps, в том, что 
# load/dump - принимают сам файл, 
# loads/dumps - принимают строку


