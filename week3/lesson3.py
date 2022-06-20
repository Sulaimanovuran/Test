#обработка исключенийб Оператор try-exept

#1) Ошибки 
    #SyntaxError
# 2f = 2
# if True

    #IdentationError - неправильный отступ
#  hello = 'привет'

    #TabError  - Смешивание пробелов и табов
# if True:
#     print('HeLLo')
#     print('hello')


#2)Исключения

#ZeroDivisionError
#2 / 0

#TypeError
#'hello' + 2


#ValueError
#age = int(input())
#int('str')


#indexError
# l = [1,2,3]
# l[5]


#KeyError
# dict_ = {'a': 'hello'}
# dict_['b']


# ModuleNotFoundError
# import math2



# AttributeError:
# age = 30
# age.lower()

#KeyboardInterrupt
# while True:
#     print('hello')


# try:
#     2 / 0
# except ZeroDivisionError:
#     print('обработали исключение')

# l= [1,2,3,4]
# try:
#     print(l2[0])
# except:
#     print('обработали')  # голое исключение

# try:
#     num1 = int(input())
#     num2 = int(input())
#     print (num1 / num2)
# except ValueError:
#     print('Вводите числа')
# except ZeroDivisionError:
#     print ('на ноль делить нельзя')


# try:
#     num1 = int(input())
#     num2 = int(input())
#     print (num1 / num2)
# except (ValueError, ZeroDivisionError):
#     print('Вводите числа на ноль делить нельзя')

# try:
#     while True:
#         print('hello world')
# except KeyboardInterrupt:
#     print ('Ctrl +c')
# print (2+2)


# try:
#     2name
# except:
#     print ('f')


# list_ = [1,2,3,4,5]
# try:
#     for i in range(len(list_) + 1):
#         list_.pop()
#     print(list_)
# except IndexError:
#     print('heh')
# print (list_)


# try:
#     age = int(input('Введите ваш возраст'))
# except:
#     age = None
#     print('вы ввели не число')
# else: # Когда в блоке try не сработало исключение
#     print('Все хорошо вы правильно ввели возраст')
# finally: # сработает в любом случае
#     print ('Я закончил обрабатывать')
# print (age)


# age = int(input('Введите ваш возраст'))
# if age < 18:
#     # raise Exception('Вы малы!')
#     raise ZeroDivisionError('Вы малы')


# age = int(input('Введите ваш возраст'))
# try:
#     if age < 18:
#         raise ValueError('Вы малы')
# except ZeroDivisionError:
#     print ('heh')
# print (2+2)


# try:
#     num1 = 2
#     num2 = 'dfg'
#     print (num1 / num2)
# except Exception as e:
#     print (e)


# try:
#      2 / 0
# except ValueError:
#     print ('Exception')
# except ZeroDivisionError:
#     print ('zero')



# Запросите у пользователя несколько слов и чисел введенных через пробел,
#  затем поместите эти слова в список,
#   переберите этот список циклом и перевидете все строки в тип данных число,
#    все числа поместите в отдельный список, а на возникающие ошибки выводите исключение:
#     'Данный элемент не является числом!'


# string = input('Введите несколько слов и чисел через пробел: ')
# list_ = []
# try:
#     for i in string.split():
#         list_.append(int(i))
# except ValueError:
#     print ('Данный элемент не является числом!')
# print (list_)


# x = input()
# y = input()
# try:
#     print(int(x) + int(y))
# except ValueError:
#     print(x + y)


# b = 10
# c = 11
# try:
#     print(a)
# except NameError:
#     print ('Нет такой переменной')

# num1 = int(input())
# num2 = int(input())
# try:
#   print(num1 / num2)
# except ZeroDivisionError:
#   print ("You can't divide by zero")

# dict_ = {'name':'John', 'age':30}
# try:
#     print (dict_['id'])
# except KeyError:
#     print('Такого ключа нет')

# l = [1,3,54,43,2,445]
# try:
#     print(l[8])
# except IndexError:
#   print('Нет элемента с таким индексом')


# from ast import expr_context


# try:
#     num1 = int(input())
#     num2 = int(input())
#     print (num1 / num2)
# except (ValueError, ZeroDivisionError):
#     print('Вы ввели не число или на ноль делить нельзя')


# from multiprocessing.sharedctypes import Value


# cash = int(input('Введите сумму которая у вас в бумажнике: '))
# try:
#     if cash < 0:
#         raise ValueError('Сумма не может быть отрицательной')
#     else:
#         print (f'У вас в бумажнике {cash} сом')
# except ZeroDivisionError:
#     print('Введите сумму больше нуля')


# from nis import cat


# try:
#     num1 = int(input())
# except:
#     print('вы ввели не число')


# try:
#     num1 = int(input())
#     num2 = int(input())
# except ZeroDivisionError:
#     print('not 0')
# except ValueError:
#     print('not str')

# dict_ = dict.fromkeys(('makers', 'bootcamp'),0)
# dict_ = {key: len(key) for key, v in dict_.items()}
# dict_.update({'except':'Excpection'})
# print(dict_)

# while True:
#     try:
#         key = input()
#         if key == 'exit':
#             break
#         dict_[key] += 2
#     except KeyError:
#         print('not this key')
#     except TypeError:
#         print('only words')
#     else:
#         print (dict_[key])
#     finally:
#         print (dict_)


# list_ =[i for i in range(1,31)]

# try:
#     index = int(input())
#     list_[index] = 'makers'
# except IndexError:
#     print('You are out of list range')
# except ValueError:
#     print('Please enter number')
# else:
#     print('There is not excpection')
# finally:
#     print(list_)


# from os import makedirs


# try:
#     print(makers)
# except NameError:
#     print('not')

# from unittest import expectedFailure


# number = int(input())
# if number not in range(1,71):
#     raise Exception:
# print ('ok')
