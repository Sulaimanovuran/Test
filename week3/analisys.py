# Dict
# Comprehensions
# Try-except
# Functions

# Словарь - изменяемыйб неупорядоченный, тип данных в котором хранятся пары ключ:значение.
# Ключ любой неизменяемый тип данных. Значение любой тип данных.


'''''
Comprehensions
Генераторы последовательности

Синтаксис:
[действие for элемент in range(1,11 if i % 2 == 0)]
[i ** 2 for i in range(1,11)]
'''''

#  Comprehensions с тернарными условиями
#  res = [True if i % 2 ==0 else False for i in range(1,11)]
#  print(res) #[False, True, False, True, False, True, False, True, False, True]

#  dict comprehensions
#  dict_ = {i: i** 2 for  in range(1,11)}
#  print (dict_)





# a = {
#     'Timur': {'history': 90, 'math': 95, 'literature': 91},
#     'Olga': {'history': 92, 'math': 96, 'literature': 81},
#     'Nik': {'history': 84, 'math': 85, 'literature': 87}
#     }
# a = {k: inner_key for k, v in a.items() 
# for inner_key, inner_value in v.items() 
# if inner_value == max(v.values())}
# print (a)

#--------------------------------------------

# a = {
#     'Timur': {'history': 90, 'math': 95, 'literature': 91},
#     'Olga': {'history': 92, 'math': 96, 'literature': 81},
#     'Nik': {'history': 84, 'math': 85, 'literature': 87}
#     }
# b = {k: k2 for k,v in a.items() for k2,v2 in v.items() if v2 == max(v.values())}
# print (b)


#######


# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# my_dict = {key: inner_key for key,value in my_dict.items() for inner_key in value.keys()}
# print (my_dict)

# #----------------------------------------------------

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# my_dict = {k:{k2 for k2 in v.keys()} for k,v in my_dict.items()}


########### comprehensions


# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3} 
# a = {k: [j for j in range(1,v+1)] for k,v in a.items()}
# print (a)


############

# import random

# set1 = {random.randint(0,10) for i in range(10)}
# set2 = {random.randint(0,10) for i in range(10)}
# set1.update(set2)
# if len(set1) < 20:
#     print(f'В этом сете было {20 - len(set1)} повторений, длина сета состаляет {len(set1)}')


###### Functions - это именованный блок кода.
###### Мы можем вызывать функцию обращаясь к нему по имени и используя круглые скобки.

'''
Позиционные
Именованные
Необязательные (*)
Ключевые (**)
'''

# def func(позиционные, с дефолтом, *args, **kwargs):
#     args = tuple
#     kwargs = dict


# def func(num):
#     res = [i for i in range(1,num+1)]
#     return res
# print (func(8))



accounts = [[1,2,3,4], [2,3,4], [3,5,7]]
def func(num):
    lst =[]
    max_ =[]
    for i in num:
        lst.append(sum(i))
        
    return max(lst)

print(func(accounts))

# comprehension
list_ = [sum(i)]