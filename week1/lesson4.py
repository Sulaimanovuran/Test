#Логический тип данных

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
    #print (0)


# num1 = int(input())
# num2 = int(input())
# if num1 / num2 == int():
#   print (num1/num2)
# else:
#   print (num1 // num2)
#   print (num1 % num2)

# year = int(input())
# if (year % 4 == 0) and (year % 100 !=0) or (year % 400 == 0):
#   print ('YES')
# else:
#   print ('NO')

# str_ = input()
# if str_ == 'Hi':
#   print ('Привет!')
# else:
#   print ('NO')
# str_ = input()
# print ('Привет!' if str_ == 'Hi' else 'NO')

from curses.ascii import isdigit


# count = 0
# str_ = input()
# if str_.isdigit():
#   count = str_
#   print (int(count))

# number = int(input())
# type_ = input('Перевести в байты (b), в килобайты (k): ')
# if type_ == 'b':
#   print (number * 1024)
# elif type_ == 'k':
#   print (number / 1024)


# m = int(input())
# n = int(input())
# k = (m * n) / int(input())
# if k % 2 == 0:
#   print ('YES')
# else:
#   print ('NO')

# h_age = int(input("Input a dog's age in human years: "))
# if h_age < 0:
# 	print("Age must be positive number.")
# 	exit()
# elif h_age <= 2:
# 	d_age = h_age * 10.5
# else:
# 	d_age = 21 + (h_age - 2)*4
# print("The dog's age in dog's years is", d_age)


# h_age = int(input('Введите возраст в человеческих годах: '))
# if h_age <= 2:
#   d_age = h_age * 10.5
# else:
#   d_age = 21 + (h_age - 2)*4
# print ('Возраст собаки в собачьих годах:', d_age)


# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if abs(x1 - x2) == abs(y1 - y2):
#     print('YES')
# else:
#     print('NO')