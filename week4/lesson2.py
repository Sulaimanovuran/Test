# str_= 'hello'
# for i in str_:
#     print(i)

# while i in str_[0:-1]:
#     print (i)


# Области видимости и пространства имен

# LEGB
    # Local
    # Encloused
    # Global
    # Built-in

# import this


# x = 'Это глобальная переменная'

# def some_func():
#     x = 'Это замкнутая переменная'
#     def some_func2():
#         x = 'Это локальная переменная'
#     return some_func2()
# some_func()
# print (x)

# x = 10

# def func():
#     print(x)
#     x+=5


# x = 10
# y = 15

# def func():
#     x = 5
#     print (x) # 5
# func()
# print (x) # 10

# x = 10
# y = 15

# def func():
#     x = 5
#     print (locals()) # {'x': 5}
# func()
# print(locals())  #'x': 10, 'y': 15


# x = 0
# def counter():
#     global x
#     x += 1
#     print (x)

# counter() #1
# counter() #2

# x = 0
# def counter():
#     global x
#     x += 1
#     print (x)

# counter()
# counter()
# counter()
# print(x)

# x = 0
# def counter():
#     global x
#     x += 1
#     # print (x is globals()['x'])
#     print (globals())
#     print(x)

# counter()
# counter()
# counter()


# x = 0
# def counter():
#     global x
#     x += 1
#     print (x)
#     def func():
#         global x
#         x += 1
#     func()
# counter()
# print (x)


# def f():
#     x = 20
#     def f2():
#         nonlocal x
#         x = 40
#     f2()
#     print (x)
# f()

# for i in range(10):
#     pass
# print (i) #9

# while 1:
#     i = 10
#     break
# print (i) # 10


# from math import pi
# print (dir(__builtins__))

# from re import A


# def outer_func():
#     global a
#     a = 20

#     def inner_func():
#         # nonlocal a
#         a = 30
#         print (a)
#     inner_func()
#     print (a)
# a = 10
# outer_func()
# print(a)


# from curses import nonl


# doll = 20
# def func1():
#     global doll
#     doll2 = 15
#     doll += doll2
#     def func2():
#         global doll
#         doll3 = 10
#         doll += doll3
#     func2()
#     print(doll)
# func1()


# counter = 0
# def increment():
#     global counter
#     counter += 1
# increment()
# print(counter)
# increment()
# print(counter)
# increment()
# print(counter)


# def foo():
#     var = 'переменная foo'

#     def bar():
#         global var
#         var = 'переменная bar'

#     bar()
#     print("переменная в foo: ", var)

# foo()
# print("переменная в foo: ", var)



# x = 'Я глобальная переменная!'
# def func():
#     global x
#     x = 'Я могу изменяться'
# func()
# print(x)
# print (globals())


# balance = 1000
# def get_salary(amount):
#     global balance
#     balance += amount
# def pay_bills(amount, log_name):
#     global balance
#     balance -= amount
#     print (f'Вы заплатили {amount} сом за {log_name}')
# def get_balance():
#     global balance
#     print(f'У вас на счету {balance}сом')

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()

# num = 3
# def mul():
#     global num
#     num *= num
# mul()
# print(num)

# mul()
# # print(num)


# result = 0

# def pow_first(x, y):
#     global result
#     result = x ** y
#     def pow_second(z):
#         global result
#         result %= z
#         return result
#     pow_second()
# pow_first(4,5)
# print (result)


# pow_second(36)
# print (result)


# name = input()
# age = int(input())

# def age_control(name, age):
#     if age <= 17:
#         return False
#     else:
#         return True
# print(age_control(name, age))


# friends = {
#     'Мурат': 24,
#     'Эржан': 21,
#     'Чынгыз': 24,
#     'Алтынай': 17,
#     'Асеме': 16}

# def age_control():
#     global friends
#     for name,age in friends.items():
#         if age <= 17:
#             print (f'Вас зовут {name}, вход запрещен')
#         else:
#             print(f'Вас зовут {name}, вход разрешен')
# age_control()



# names = ['john', 'sam', 'alice', 'winston', 'sherlok']
# def right_names():
#     names2 = [i.title() for i in names]
#     return names2
# print(right_names())


# list_ = ['a', 'e', 'y', 'u', 'i', 'o']
# counter = {'Цифры': 0, 'Буквы': 0, 'Спец.символы': 0}
# def func(str_):
#     for i in str_:
#         if i.isdigit():
#             counter['Цифры'] += 1
#         elif i.isalpha():
#             counter['Буквы'] += 1
#         else:
#             counter['Спец.символы'] += 1
# func('345j34jjdfsfd=-;l.,')
# print(counter)




# list_ = ['a','e','u','i','o','y']
# counter = {'Гласные': 0, 'Согласные': 0, 'Прочее': 0}
# def func(str_):
#     for i in str_:
#         if i.isalpha() and i in list_:
#             counter['Гласные'] += 1
#         elif i.isalpha() and i not in list_:
#             counter['Согласные'] += 1
#         else:
#             counter['Прочее'] += 1
#     return counter

# print(func('Makers! Bootcamp!'))


# list_ =list()
# list_ = [i for i in range(11)]
# print(list_)

# list_ = [1,2,67,432,5,7,22,4,7,9]
# list_ = [i for i in list_ if i < 7]
# print(list_)



# x1 = 20
# res = 0
# def func1():
#     global x1, res
#     x2 = 15
#     res = x2 + x1
#     def func2():
#         global x1, res
#         nonlocal x2
#         x3 = 10
#         res = x1 + x2 + x3
#     func2()
#     return res
# print (func1())


# names_ = []


# def add():
#     add_name = input('Введите имя которое хотите добавить: ')
#     names_.append(add_name)
#     return names_

# def remove():
#     rm_name = int(input('Введите индекс имени которое хотите удалить: '))
#     names_.pop(rm_name)
#     return names_


# add()
# add()
# add()
# remove()
# add()
# remove()
# remove()
# add()
# add()
# remove()
# print (names_)


# def color_check():
#     day = int(input('Введите нужное число месяца: '))
#     if day % 2 == 0:
#         print('Красная футболка')
#     else:
#         print('Синяя футболка')

# color_check()

# num1 = int(input())
# num2 = int(input())

# if num1 % num2 == 0:
#     print (f'Число {num1} делиться на {num2} без остатка. Результат {num1/num2}')
# else:
#     print (f'Число {num1} не делиться на {num2} без остатка. Результат {num1//num2} , {num1 % num2}')


# num1, num2, num3 = 45,67,54
# if num1>num2 and num1 > num3:
#     print (num1)
# elif num2 > num1 and num2 > num3:
#     print(num2)
# else:
#     print(num3)

# numbers = [1,3,4,6,8,14,20,11]
# def func():
#     new_nums = [i ** 2 for i in numbers]
#     return new_nums
# print(func())

# import math
# print (math.factorial(5))
# nums = [1,2,3,4,5]
# for i in nums:
#     fact = 1
#     new_nums = []
#     for j in range(1,i+1):
#         fact = fact * j
#         new_nums.append(fact)
# print (new_nums)
# new_nums = [math.factorial(i) for i in nums]


# def factor():
#     new1_nums = []
#     for i in nums:
#         for j in range(1,i+1):
#             new1_nums += j
#     print(new1_nums)

# factor()

# list_ =[1,2,3,4,5,6]
# list_1 =[]
# for i in range(1,10):
#     if i % 2 == 0:
#         list_1.append(i)


# print (list_1)

# num = -45
# if num < 0:
#     print (True)
# else:
#     print (False)




# num = 3
# def func():
#     global num
#     num = 5
#     print (num)
# func()


# print(num)


x = int(input())
y = int(input())

if x % y ==0:
    print(x/y)
else:
    print(x//y, x%y)