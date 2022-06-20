# Втроенные функции lambda, map, filter


# map - встроенная функция которая нужна для того чтобы применить 
# какую-либо функцию к итерируемому обьекту

# lambda - анонимная функцияб которая применяется только один раз

# Функция высшего порядка - это фунуция которая может принимать в качестве аргумента другую функцию
# и\или возвращать функцию как результат работы

# list_ = [1,2,3,4,5]
# def func(x):
#     return str(x)

# result = list(map(func, list_))
# result2 = list(map(lambda x: str(x),list_))
# result3 = list(map(str,list_))
# print (result)
# print (result2)
# print (result3)


# list_ = range(0,10)

# def func(x):
#     return x+10

# result = list(map(func, list_))
# result2 = list(map(lambda x: x +10, list_))
# print (result)
# print (result2)


# list_ = [1,2,3,4,5,6]

# def func(x):
#     if x % 2 == 0:
#         return 'четное'
#     else:
#         return 'нечетное'

# res = list(map(func, list_))
# print (res)
# res2 = list(map(lambda x: 'четное' if x % 2 == 0 else 'нечетное', list_))
# print(res2)

# list_ = ['1', '2', '3', '4']
# def func(x):
#     return int(x)


# res1 = list(map(func, list_))
# print(res1)

# res2 = list(map(int, list_))
# print (res2)

# res3 = tuple(map(lambda x: int(x), list_))
# print (res3)



# filter - функция для фильтрации

# list_ = [1,2,3,4,5,6,7]

# res1 = list(filter(lambda x: x > 3, list_))
# res2 = list(map(lambda x: x > 3, list_))
# def f(x):
#     if x > 3:
#         list_.append(x)
#     return list_
# res3 = list(filter(f, list_))
# print(res2)
# print(res3)

# list_ = range(100)
# def f(x):
#     if x != 0:
#         return x

# res1 = list(filter(f, list_))
# print (res1)

# res2 = list(filter(lambda x: x % 2 != 0, list_))
# print (res2)


# str_ = 'hello'

# res1 = list(map(lambda x: str_ + ' ' + x, str_))
# print(res1)


# str_ = 'aaaaaaaaabbbbbbbbbbbbccccccccccccccceeeeeeeeeeee'
# res1 = set(filter(lambda x: x != 'b' and x != 'c', str_))
# print(res1)

# i = 0
# while i < 3:
#     if rafael[0] > novak[0]:
#         res_r += 1
#     else:
#         res_n += 1


# i = 0
# import functools
# rafael = [3,0,2]
# novak = [2,2,1]
# res_r = 0
# res_n = 0
# for i in range(1,4):
#     if functools.reduce(map(lambda p, q: p < q, rafael,novak)):
#         res_r +=1
#     else:
#         res_n +=1
# # print(functools.reduce(lambda x, y : x and y, map(lambda p, q: p > q, rafael,novak), True))
# print (res_r)
# print(res_n)

# rafael = [3,0,1]
# novak = [2,2,1]
# res_r = 0
# res_n = 0
# for a_,b_ in zip(rafael,novak):
#     if a_> b_:
#         res_r +=1
#     else:
#         res_n +=1

# print(res_r)
# print(res_n)

# import itertools
# x=[0.1, 1, 2.5, 4, 5]
# N = 5
# res = []
# for i in range(len(x)):
#     for el in itertools.combinations(x, i+1):
#         if(sum(el)<=N and N-sum(el) < min([el_sub for el_sub in x if el_sub not in el] or [N])):
#             res.append(el)
# print(el)


# x, y, z = 1,1,2
# def func():
#     list_ =[x,y,z]
#     res = list(set([(x,y,z) for x in list_ for y in list_ for z in list_ if x+y+z != 4]))
#     return res
# print (func())

# list_ = [1,2,3,4,5,6]
# res = list(map(lambda x: x ** 2,list_))
# print(res)


# list_ = [-1, 2, 3, 0, 5, -3, 7,]
# res = list(map(lambda x: True if x > 0 else False, list_))
# print (res)

# nums = [2,4,5,6,677,89,42,4667]
# nums = list(filter(lambda x: x% 2 == 0, nums))
# print (nums)

# str_ = ['hello', 'world', 'makers', 'bootcamp', 'makersapce', 'slepaya pecahat']
# str_ = list(filter(lambda x: len(x) > 7, str_))
# print(str_)

# from asyncio import events


# nums = [2,4,5,6,677,89,42,4667]
# even = 0
# odd = 0
# def func():
#     global even,odd
#     for i in nums:
#         if i % 2 == 0:
#             even +=1
#         else:
#             odd +=1
#     return f'Четные {even},нечетные {odd}'
# print(func())


# ev = list(map(lambda count(x): x %2 ==0, nums))

# from functools import reduce
# srt_ = 'makers'

# res = list(reduce(lambda a,b: a + b, srt_))
# print(res)

from functools import reduce
# list_ = [5,6,7,8]
# list_ = reduce(lambda a,b: a*b, list_)
# print(list_)

# names = ['John', 'Amanda', 'Sam', 'Alice', 'Sherlock']
# longest_name = reduce(lambda a,b: a if len(a)>len(b) else b, names)
# print(longest_name)

print(dir(tuple))