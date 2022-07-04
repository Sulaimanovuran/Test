# import random
# def get_info():
#     name = input()
#     last_name =input()
#     def get_info():
#         nonlocal name, last_name
#         password = [name + last_name + i for i in random.choices(range(10), 7)]
#         return password

#     get_info()

# print (get_info())
# def get_info():
#     name = input()
#     last_name =input()
#     def get_info():
#         nonlocal name, last_name
#         password = ''.join(([name + last_name] + [random.choice('0123456789') for i in range(10)]))
#         print(password)
#     get_info()

# get_info()


# L - видит все (тело функции)
# E - Global, Built-in (внешняя функция)
# G - Built-in (все на уровне исполняемого файла)
# B - (мы не видим его)



# words = ['level', 'hello', 'down', 'aba']

# res = list(map(lambda x: x if x == x[::-1] else None, words))
# print (res)

# res1 = list(filter(lambda x: x == x[::-1], words))
# print(res1)


# list_ = ['123', '12qee', '234dsf', '342']
# res = list(filter(lambda x: x.isdigit(), list_))
# new_res = int(res)
# print (new_res)

# n = int(input())
# lst=[2]
# for i in range(3, n+1, 2):
# 	if (i > 10) and (i % 10==5):
# 		continue
# 	for j in lst:
# 		if j*j-1 > i:
# 			lst.append(i)
# 			break
# 		if (i % j == 0):
# 			break
# 	else:
# 		lst.append(i)
# print (lst)
# print(dir(set))

# str_ = 'makers bootcamp courses'
# print (str_.split())


# print(pow(5, 3))
# print(124%4)


# l = {'r': 1, 'l':3, 'n':5}
# l.setdefault('v')
# l.pop('r')
# print (l)


# divided = [x for x in range(100) if x % 2 == 0 if x % 6 == 0]
# print(divided)
# a = 1
# b = 0
# if a == b:
# print('Hello world')

# def check():
#     x = 0
#     x = 1 * 2
#     print (x)

# print(locals())
# hello('makers')

# name = 'Sandy'
# def func_one():
#     name = 'Andy'
#     def func_two():
#         name = 'Mandy'
#         print(name)
#         print(locals())
#     func_two()
# func_one()

# except Exception as n:
#     p


'''
Втроенные функции

map(func, iterible object)
'''

# list_str = ['1', '2', '3', '4']
# list_int = []

# for i in list_str:
#     list_int.append(int(i))

# list_int = list(map(int, list_str))
# print (list_int)

# def dollars_to_soms(dollars:int) -> int:
#     return f'{round(dollars * 84.80)} soms'

# dollars = [100, 50, 25, 90, 65]

# soms = list(map(dollars_to_soms, dollars))
# print(soms)

'''
lambda
'''

# print((lambda x: x ** 2) (56))
# square = lambda x: x ** 2
# print(square(56))

# print((lambda x,y,z: x+y+z)(1,2,3)) # 6

# list1 = [1,2,3]
# list2 = [4,5,6]
# list3 = [7,8,9]
# new_list = list(map(lambda x,y,z: x + y + z, list1, list2, list3))
# print(new_list) #[12, 15, 18]


# num_list = [2,4,6,8,9,5,3,3]
# num_list2 = list(map(lambda x: x * 2, num_list))
# print(num_list2)

'''
filter
'''

# nums = [12,4,4567,89,45,34,2]

# fil_nums = list(filter(lambda num: num % 3 == 0, nums))
# print(fil_nums)


# dict_ = [{'subject': 'Python', 'point': 89}, {'subject': 'js', 'point': 92}, {'subject': 'Python', 'makers': 100}]

# new_dict = list(filter(lambda x: x['subject'] == 'Python', dict_))
# print(new_dict)

# users = [
#     {'username': 'Alice123', 'comments': ['i love it', 'good']},
#     {'username': 'sam45', 'comments': []},
#     {'username': 'john', 'comments': []},
#     {'username': 'Raychel','comments': ['i like it']}]

# active_users = list(filter(lambda x: x.get('comments', None), users))
# inactive_users = list(filter(lambda x: not x.get('comments', None), users))
# print(active_users)
# print(inactive_users)

# names = ['Alice', 'Sandra', 'Molly', 'Tim', 'bill', 'ann']
# greetings = list(map(lambda name: f'Welcome, {name}', filter(lambda x: len(x)>= 5, names)))
# print(greetings)

'''
reduce(func, iterible object)
'''

# from functools import reduce

# numbers = [1,2,3,4]

# sum_ = functools.reduce(lambda x, y: x + y, numbers)
# print(sum_)               #1+2_|  |_3


# numbers  = [78, 5, 45,23, 54656, 456, 456, 345, -435, -45324]
# max_ = functools.reduce(lambda a, b: a if a > b else b, numbers)
# print(max_)


# numbers = [5,6,8,1,2]
# multiplay = reduce(lambda x, y: x * y, numbers)
# print(multiplay)


'''
zip()
'''
# list_a = [1,2,3,4,5]
# listb = ['a', 'b', 'c', 'd', 'e']
# listc = ['makers', 'bootcamp', 'hello', 'world', 'zip']
# list_ = list(zip(list_a, listb, listc))
# list1, list2, list3 = list(zip(*list_))
# print(list1, list2, list3)



# print(dir(__builtins__))

'''
enumerate()
'''

# seasons = ['spring', 'winter', 'fall', 'summer', 'makers', 'bootcamp']
# enumerated_seasons = dict(enumerate(seasons, 5))
# print(enumerated_seasons)

'''
abs
'''
# negative = -123
# absolute = abs(negative)
# print(absolute)

'''
all, any
'''
# list_ = [0,0,0,0,0]
# is_true = all(list_)
# print(is_true) #False


# list_ = [0,0,2,0,0]
# is_true = any(list_)
# print(is_true) # True

'''
ascii()
ord()
chr()
'''

# list_1 = ['makers', 'мейкерс', 23 , 0, '$*']
# list_2 = ascii(list_1)
# print(list_2)  -> ['makers', '\u043c\u0435\u0439\u043a\u0435\u0440\u0441', 23, 0, '$*']


# print(ord('f')) -> 102
# print(chr(102)) -> f

'''
divmod()  ->  tuple  -> (x//y, x%y) 
'''

# print(divmod(15, 7)) -> (2,1)