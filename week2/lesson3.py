# count_ = 0
# while True:
#     count_+=1
#     print (count_)
# play = True
# while play:
#     num1 = int(input('nu1: '))
#     num2 = int(input('nu1: '))
#     operation = input('Введите + или - : ')
#     if operation == '+':
#         print(num1 + num2)
#     elif operation == '-':
#         print (num1-num2)
#     else:
#         print('Такой операции нет')
#     f = input('Хотите завершить работу? (Yes)')
#     if f == 'Yes':
#         play = False
#         print ('seeyou')

# list_ = ['hello', True, 'Sam']
# i = 0
# while i < len(list_):
#     print (list_[i])
#     i+=1

# list_ = ['hello', True, 'Sam']
# for i in list_: # for -- используется для перебора
#     print (i)


# text = 'hello world'
# for i in text:
#     print (i)


# for i in range(5):
#     print(i)

# for i in range(1,6):
#     print (i)

# for i in range(0,100,2):
#     print(i)

# list_ = list(range(100))
# print (list_)

# for i in range(5):
#     if i == 3:
#         continue
#     print (i)

# list_ = []
# list_2 = []
# for i in range(101):
#     if i % 2 == 0:
#         list_.append(i)
#     else:
#         list_2.append(i)
# print (list_)
# print(list_2)

# list_ = ['Alex', 'John', 'John', 'tom', 'Snow']
# for i in list_:
#     if i == ('Snow'):
#         print ('Пока',i)
#     else:
#         print('Hi',i)


# list_ = [[1,2], [1,2,3], ['hello']]
# for i in list_:
#     print (f'start{i}')
#     for j in i:
#         print (j)
#     print(f'end {i}')

import random
# print (random.randit(0, 10))

# list_ = []
# for  i in range(100):
#     list_.append(random.randint(0, 10))
# print (set(list_))

# for i in range(21):
#     if i % 2 == 0:
#         print(i ** 2)
#     else:
#         print(i**5)

# a = [1,3]
# print(int(a))


# list_ = []
# for i in range (0, 15):
#     list_.append(i)
# print (list_)

# list_ = [23,45,2,12,344,42,31,34]
# list_2 = []
# list_3 = []
# for i in list_:
#     if i % 2 == 0:
#         list_2.append(i)
#     else:
#         list_3.append(i)
# print (list_2)
# print (list_3)

# a = int (input())
# f = 1
# for i in range (1, a+1):
#     f = f*i

# print (f)


# for i in range(1,11):
#     print(i**2)

# users = ['Alce', 'Sam', 'Carly']
# for user in users:
#     print (f'Hello {user}')


# guests  = []
# list_lenght = (int(input('enter number of guests: ')))

# for i in range(list_lenght):
#     user = input('enter guest name: ')
#     guests.append(user)

# print (guests)
# import math
# l = [1,2,3,4,5]
# l2 = []
# for i in l:
#     l2.append(math.factorial(i))
# print (l2)



# numbers = [3,5,7,45,89,34,23]
# numbers2 = []
# f = 1
# for i in numbers (range(1, numbers + 1)):
#   f = range(f*i)
#   numbers2.append(f)
# print (numbers2)

# l1 = [1,2,3,4,5,6]
# l2 = []
# for i in l1:
#   l2.append(i)
# print (l2)

# l= []
# for i in range(0,11):
#   l.append(i)
# print(l)

# l = (1,3,5,7,9,6,5,3,233,456,47,78)
# for i in l:
#   if i > 7:
#       print (i)

# name_of_list = ['Helloworld']
# new_list = []
# name_of_list=''.join('')
# print(name_of_list)

# list_ = ['hello', 'world']
# new_list = []
# list_.reverse()
# new_list.append(list_)
# print(new_list)

# list_ = ['hello', 'world']
# new_list = []
# list_.reverse()
# for i in list_:
#     new_list.append(i)
# print(new_list)

list_ = [range(0,20)]
print(list_)
