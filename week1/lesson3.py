# Тип данных: string (строки)

#  Строка - это последоваельный набор символов, котоый состоит из: (букв символов, разделителей и тд)
# Строка то неизменяемыйиндексируемый, упорядоченный,  тип данных
# PEP=8

# name = 'john'
# last_name = 'snow'
# full_info= name + " " + last_name #конкатенация - сложение строк ( "h" + "l")
# print(full_info)
# age = 30
# # print (full_info) + " " + (str( age))
# text = "dfdsfsdfsdfsdasfdfdas"
# print (len(text))
# print (text * 5)
# hello = "hello"
# print (hello[0])
# print (hello[-1])


#Срезы(Slice)

# print = "hello" # не может иметь место так как слово зарезервировано командой
# test_text = 'helo world'
# print (test_text [0:5]) # hello вывести отрезок слова "СРЕЗЫ"
# #[от:до]
# print (test_text [0:]) # h
# print (test_text[0;5;2]) # [от:до:шаг] hlo
# print (test_text [0:5:3]) #hl
# test_text = 'hello world'
# print (test_text [0:-2])
# print (test_text [::-1]) #dlrow olleh


#  экранированная последовательочсть - это последовательности которые начинаются с символа "\" за которым следует один или более символов


# print( 'hello\n world') #перенос на следующюю строку
# print ( 'hellooo\ra') # возврат каретки
# print ('hello\t world') # ТАБУЛЯЦИЯ 4 пробела
# info = " \t это табулция"
# info2 = '\\t это табуляция' #отменить \t
# print (info2)
# print ('it\'s') # it's

# from os importmakedirs, 
# text = makedirs
# text = 'makers'
# print (text [0])
# print ('text' [0])
# text = 'makers'
# print (text [-1])
# print ('makers'[-1:-2])
# print ('makers'[4:])
# print (text [::-1])
# t1 = 'makers'
# t2 = 'courses'
# print (t1 + " " + t2)
# t1 = 'yeep'
# print (t1 * 4)
# t1 = 'themakerscoursesthebestcoursesintheworld'
# print (t1.replace ('o', '*'))
# print ("The quick brown fox jumps over the lazy dog".replace ('o', '*'))
from functools import update_wrapper

# text = 'shower'
# print (text.upper())
# text = 'makers'
# print (text.upper())
# t1 = 'LOWER'
# print (t1.lower())
# text1 = 'ulan'
# print (text1.upper())
# text2 = 'MEKEN'
# print (text2.lower())
# name = (input ('введите ваше имя:'))
# age = int(input('введите ваш возраст:'))
# print ("привет", name, "тебе", age, "лет")
# text = 'makers'
# print (text [-1] + text [1:5] + text [0])
# t = 'makers'
# print (t [-1] + t[1:5] + t[0])
# print( 'hello\n world')
# text = "#makers#bootcamp#программирование#it#курсы"
# print (text.split ('#') [1:])
# name = input("Введите ваше имя:")
# last_name = input ("Введите вашу фамилию:")
# age = input("Сколько вам лет:")
# city = input("В каком городе вы проживаете:")
# print (f'Привет. Вас зовут ' + name + " " + last_name +' вам ' + age + ' лет. Вы проживаете в городе:' + city)
# print ('makers bootcamp '[1::2])
# print ('abracadabra'.replace ('c', 'K'))
# print ( 'hellooo\ra')



# методы строк
# text = 'some text'
# print (dir (text))
# print ('text'.islower)
import math
# print (dir(math))
# text = 'stroka'
# print (text.isalpha()) #проверяет сосотоит ли строка тоьлко из букв
# print (text.isdigit()) # только из цифр
# print (text.islower()) #проверка нижнего регистрa


# some = input ('введите строку')
# print (some.islower())

# hello = 'Hello World'
# print (hello.replace ('l', '#'))

# print (hello.replace('l', '#', 1)) # (шаблон, замена [maxcount])


# s = input(' введите строку')
# s = s.replace('a', '').replace ('A', '')
# print(s)



# str_ = 'hello, world,name,ff'
# str_ = str_.split(',')
# print(str_)
#some_text = 'hello world myname is vlad'
#print (some_text.split()) 
# print ('text'.upper())
# print ('hello'.lower())
# print ('hello'.title ())
# str_ = 'hello my name is uran'
# print (str_.count('a')) #2
# print (str_.count(''))


# s= 'heh'
# print(s.count('h',1)) #1
# print(s.count('h',1, 1))# 0 count(str[start],[end])

# some_text = 'h d hs jd gn '
# print (some_text.strip()) #удалить пробелы в начале и конце
# print (some_text.rstrip()) #удалить пробелы с права
# print (some_text.lstrip()) #с лева
# print (some_text.strip())

# email = 'admin@admin.com'
# print (email.endswith('com')) # проверить заканчивается ли слово на указанную
# print (email.startswith('admin')) # начинается ли
  

# str_ = 'hello is hello si uranis'
# # print (str_.count('is')) # проверить количество
# list_ = str_.split() #превратить в список
# print (type(list_)) 
# hello = ' '.join(list_)

# name = input('введите ваше имя:')
# age = int(input('введите ваш возраст:'))
# email = input('введите ваш email')

# if email.endswith('.com'):
#     print (f'здравствуйте, вас зовут-{name}, Вам {age} лет, Вы зашли на {email} почту')

# str_ = 'key world hello'
# print (str_.split('  '))
# print(str_.join(str_))
# txt = ''.join(str_)
# print (txt)
# print(ord ('a')) # уникальное значение
# print (ord ('а')) 
# print (ord ('*'))
# print (chr (98)) #
# name = "john"
# password = "1"
# password2 = input ()

# if password == password2:
#     print (f'привет:, {name}')

# print ('makers\rs')
# text = "#makers#bootcamp#программирование#it#курсы"
# print (text.split ('#') [1:])
# name = input("Введите ваше имя:")
# last_name = input ("Введите вашу фамилию:")
# age = int(input("Сколько вам лет:"))
# city = input("В каком городе вы проживаете:")
# print (f'Привет. Вас зовут: {name} {last_name}, вам {age} лет. Вы проживаете в городе: {city}')
# print ('abracadabra'.replace ('c', 'K'))
# print (dir(math))
# print (dir (random))
from random import *
# print (randint(5, 100))
# # print (''.join([choice(list ('!@$%^^&*%^&*^%$^&*JFHDSKFNJSDKFGMSDF;OAKLSFNjkdfk;ajhk;sdfjksndf6+5646546541234561321789765454')) for x in range (4)]))
# print (choice ('makers'))

# x = 'America'
# y = 'Japan'
# c= x.split(); y.split(); 
# g = x + y
# print ('\r'.join([str(z) for z in g]))
# str_ = 'key world hello'
# print (str_.split('  '))
# print(str_.join(str_))
# txt = ''.join(str_)
# # print (txt)
# name = input()
# last_name = input()
# age = int(input())
# city = input()
# print(f'Вас зовут {name} {last_name}, ваш возраст {age}, вы проживаете в городе {city}')
# hello = 'Hello World'
# # print (hello.replace ('l', '#'))

# print (hello.replace('l', '#', 1))






#bool неизменяемый тип данных содержащий только два значения
#True => 1
#False => 0

# num1 = 10
# num2 = 5
# print (num1>num2) #True
# print (num1<num2)#False
# print ( 5>=5) #True
# print (4<=4) #True
# print (num1 == num2) #равно
# print (num1!=num2) #неравно

# print ('az' > 'ahello')
# print (ord ('a'))
# print (len('az') > len('ahello'))

# some_str = 'hello'
# print('helo' in some_str) #False
# print('l' in some_str) # True


#not and or
# print (not True) #False
# print (not False)# True

# print (True and True) # 

# age = 19
# name = 'John'
# print (age > 18 and name == 'John')

# # print (True and False) #False

# print (age > 18 and name == 'Steve')
# # print (False and True) #False
# # print (False and False) #False
# print ( age > 50 and name == 'John')


# age = 19
# name = 'John'
# print (age > 18 or name == 'John') # True
# print (age > 40 or name == 'John') # True
# print (age > 18 or name == 'Steve') # True
# print (age > 40 or name == 'Steve') # False


# print ((True or False) and True) # True
# print ((True or False) and False)# False
# print ((False == False) and True) # True
# a = 'hello'
# b = 'hello'
# print (a is b) #True, is сравнивает по id

# list_ = [1,2,3]
# list_2 = [1,2,3]
# print (list_ == list_2) #True
# print (list_ is list_2) #False

# #NoneType
# res = None #None = ничего, пустота
# # Условные операторы
# AGE = 28
# NAME = 'john'

# age = int(input('ваш возраст:'))
# name = input('ваше имя:')
# if age >= AGE and name.lower() == NAME:
#     print (f'привет {name.title()}, ты вип клиент!')
# else:
#     print('Вы не не подходите')
# print ('пока')


# num1 = int(input('Введите первое число'))
# num2 = int(input('Введите второе число'))
# operator = input('Введите оператор(+,-,*,/):')
# if operator == '+':
#     print (num1 + num2)
# elif operator == '-':
#    print(num1 - num2)
# elif operator == '*':
#     print(num1 * num2)
# elif oprator == '/':
#     print (num1 / num2)
# else:
# #     print ('нет такого опрератора')
# if 1:
#     print ('hello')
# print(bool(1))
# print(bool(0))
# print (bool(1000))
# print(bool(-1))
# print(bool(None))
# num = int(input())
# if num > 5:
#   print ('True')
# else:
#   print ('False')
# str_ = input()
# if len(str_)>=5:
#   print ('True')
# else:
#   print ('False')
# num = int(input())
# if num >= 90:
#     print('отлично ваша оценка 5')
# elif num >= 80:
#     print('здорово ваша оценка 4')
# elif num >= 70:
#     print('хорошо ваша оценка 3')
# elif num >= 60:
#     print('вам стоит подучить материал')
# else:
#     print ('вы не сдали экзамен')
# num = int(input())
# if num <=-1:
#     print('negative')
# elif num > 0:
#     print ('positive')
# elif num == 0:
#     print ('zero')
# num1 = 5
# num2 = 7
# num3 = 1
# print (min(num1,num2,num3))
# num1 = 6
# num2 = 7
# num3 = 6
# if num1 == num2 == num3:
#     print(3)
# elif num1 == num2 or num1 == num3 or num2 == num3:
#     print(2)
# else:
#     print(0)