import random
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