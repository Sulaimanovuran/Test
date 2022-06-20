# Словари(dict) + Методы словарей
# Изменяемый, итерируемый, упорядоченный тип данных

#{} - Литералы
# {key: value} - Синтаксис

# dict_ = {
#     'name':'john',
#      'age': 30,
#       'id': 1,    #  Ключи должны быть уникальными и неизменяемыми типами данных
#       'name': 'Vlad'   #{'name': 'Vlad', 'age': 30, 'id': 1}
#     }
# print(dict_['age'])  # Всегда обращаться по ключу


# dict_ = dict()  #создать пустой словарь
# dict_ = dict(name = 'john', age = 30, )  # добавить элементы в словарь/ нельзя добавить кючи  в виде цифр

# dict_ = {
#     'name': 'John',
#     'hobby': ['fishing', 'football']
# }
# import copy
# dict_.clear
# dict_2 = dict_
# dict_2 = dict_.copy()
# dict_2 = copy.deepcopy(dict_)
# print (dict_)

# list_= ['john', 'sam', 'steve']
# dict_ = {}
# dict_ = dict_.fromkeys(list_, True)
# dict_2 = {}
# dict_2 = dict_2.fromkeys(['hello'])
# print (dict_2)

# dict_ = {
#     'name': 'John',
#     'hobby': ['fishing', 'football']
# }

# print (dict_['name'])
# print (dict_(id)) #Error
# print(dict_.get('id')) # Проверканаличи ключа
# print(dict_.get('id', 'нет такого ключа'))

# dict_.pop('name')
# dict_['age'] = 30
# remowed = dict_.pop('age')
# print (dict_)
# print (remowed)

# dict_ = {
#     'name': 'John',
#     'hobby': ['fishing', 'football']
# }

# r = dict_.popitem() 
# print (r)
# print (dict_)

# dict_ = {
#     'name':'John'
# }
# name = dict_.c('name')
# age = dict_.setdefault('age', 30)
# # dict_.setdefault('age', 30)
# print (dict_)

# dict_ = {
#     'name': 'john',
#     'age': 30,
#     'status': True,
#     'hobby': 'fishing'
# }
# print (str(dict_.keys()))
# print (dict_.keys())
# print (dict_.values())
# print (dict_.items())

# # for i in dict_.keys(): # keys
# for i in dict_: # keys
#     print (i)


# for i in dict_.values():
#     print (i)  # values

# for i in dict_.items():
#     print (i[0])  #keys
#     print (i)


# for i, j in dict_.items():
#     print (f'key - {i}, value- {j}')
   

# d = {
#     'name': 'john',
#     'bool_': [True, False]
# }

# for i in d.values():
#     for j in i:
#         print (j)



# d = {
#     'name': 'john',
#     'id': 30
# }


# d2 = {
#     'name': 'sam',
#     'id': 1
# }

# d.update(d2)
# print (d)

# admin = {
#     'id': 1,
#     'name': 'John',
#     'password': 'admin123'
# }

# name = None
# password = None
# count_ = 3
# while admin['name'] != name:
#     name = input()

# print(f'привет {admin["name"]}. Скажи кодовый пароль у тебя 3 попытки!')
# while admin['password'] != password:
#     if count_ ==0:
#         break
#     password = input(f'У тебя осталось {count_} попыток!')
#     count_ -= 1

# dict_ = {
#     'name':'john',
#      'age': 30,
#       'id': 1,    #  Ключи должны быть уникальными и неизменяемыми типами данных
#       'name': 'Vlad'   #{'name': 'Vlad', 'age': 30, 'id': 1}
#     }
# print(list(dict_.keys())[0]) 

# dict_ = {'name': 'John', 'age': 30}
# print (list(dict_.keys())[0])

# dict_ = {
#   'name':'john',
#   'id': 34
# }
# dict_.setdefault('age', 30)
# print(dict_)
# dict_ = {
#   'name':'John',
#   'age':30
# }
# dict_.clear()
# print(dict_)

# dict_ = {
#   'name': 'John',
#   'age': 30,
#   'hobby':'fishing'
# }
# print(list(dict_.keys()))

# dict_ = {
#   'name': 'John',
#   'age': 30,
#   'hobby':'fishing'
# }
# dict_2 = {}
# dict_2 = dict_.copy()
# print(dict_2)

# dict_ = {
#   'name': 'John',
#   'age': 30,
#   'hobby':'fishing'
# }
# for keys in dict_.keys():
#   print(keys)
  

# dict_ = {
#   'name': 'John',
#   'age': 30,
#   'hobby':'fishing'
# }
# for values in dict_.values():
#   print(values)

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# for keys,values in a.items():
#   if  values % 2== 0:
#     a[keys] = 2
# print(a)
# list_= ['john', 'sam', 'steve']
# dict_ = {}
# dict_ = dict_.fromkeys(list_, True)
# print (dict_)

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# for key, values in a.items():
#   if values == None:
#     a = a.pop(key)
# print (a)

# dict_= {
#   'апельсин':45,
#   'яблоки':65,
#   'груша':115
# }
# for k, v in dict_.items():
#   dict_[k] = v // 5
# print (dict_)


  

  # dict_ = dict_.fromkeys(list_, True)

# a = {'a': 2, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# print (sum(list(a.values())))

# dict_= {
#   'апельсин':45,
#   'яблоки':65,
#   'груша':115
# }
# for k,v in dict_.items():
