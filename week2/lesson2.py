# Тип данных - list(Списки)+Методы списков

#list - изменяемый, упорядоченный, итерируемый тип данных.

# list_ = ['Alex', 'John', 'Sam']
# print (list_[1])
# list_2 = []


# list_4=[1, True, 'John', [1,2,3,['Sam']]]
# print (list_4[3]) #[1, 2, 3, ['Sam']]
# print (list_4[3][1]) # 2
# print (len(list_4)) # 4
# print (list_4[3][3][0]) # Sam

# list_ = []
# # print (list_)
# list_.append(True)
# print(list_)

# list_1 = [True, 1]
# list_2 = [False, 0]
# list_1.extend(list_2) #расширяет список
# print(list_1)
# print(list_2)

# list_.insert(0, 2)
# list_.insert(3, 'hello')
# print(list_)
# print(list_[0] + list_[1])
# list_ = [1,2,3,1]
# list_.remove(1) #удаляет по значению,только одно вхождение
# print (list_)

# list_= [True,2,3,'Hello']
# list_.pop() #удаляет по индексу
# list_.pop(0)
# list_.pop(6) #eror
# print(list_)
# remowed = list_.pop(3)
# print(remowed)
from pickle import FALSE


# list_ = [True,False,1,2,3,4,True]
# print  (list_.index(False))
# print(list_.index())
# list_2 = ['hello','john','s','w','s']
# print (list_2.index('s',3)) #4

# list_ = [1,2,3,4]
# list_.reverse()
# print(list_)

# lisr_ = [1,45,2,6,7,2,4]
# lisr_.sort()
# print (lisr_)

# list_2 = [1,2,'3'] #Eror сортирует данные только одного типа
# list_3 = ['a','b','aa','ab']
# list_3.sort(reverse=True) #сортировка в обратном порядке
# print(list_3)

# list_ = ['a','b','a','hello']
# print(list_.count('a')) #кол-во заданных символов
# print(list_.count('hello')) #1

# List = ['a','b','ab','aa']
# # print(sum(List))
# print(max(List))
# # print(min(List))
# l1 = [1,2,3,4,5,6]
# # print (id(l1))
# l2=l1
# print(id(l1))
# print(id(l2))
# l2.pop()
# print (l1)
# print (l2)
# l1 = [1,2,3,4,5,6,['hello', 'hello2']]
# l2 = l1.copy() ПОВЕРХНОСТНОЕ КОПИРОВАНИЕ
# l2[6][0] = 'John'
# print(id(l1[4]))
# print(id(l2[4]))
# print (l1)
# print (l2)
import copy
# l1 = [1,2,3,4,['hello','hello2']]
# l2 = copy.deepcopy(l1) # ГЛУБОКОЕ КОПИРОВАНИЕ
# l1[4][0] = 'Uran'
# print (l1)
# print (l2)
# l2.clear()
# l = ['a', 'b', 'c']
# s = " ".join(l)
# print (s)

# names = input('Ввfgfg


# a = 2
# a+=2 # a = a + 2
# print(a)

# num1 = 7
# num2 = 6
# res = 'Больше' if num1 > num2 else 'меньше'
# print (res)
# l = [1,2,3,4,5,6]
# print (l[0])
# # print (l[5])
# l = ['a', 'b', 'c', 'd', 'e']
# print (l[0], l[2], l[4])
# names = ['john', 'stewe', 'sam']
# names [2] = 'Van Rossum'
# print (names)
# cars = ['honda', 'bmw', 'mercedes']
# print ('my favorite car a' + cars[2].title())

# l = 'bootcamp makers'
# l = l.split(' ')
# print (l[1]+ ' '+ l[0])
# x = [32,45,3,1,23]
# y = [42,4,45,3242,34]
# x.extend(y)
# print(max(x))

# s = ['dfjgkelsmvefer']
# l=''.join(s)
# s1 = l[8:-1] + l[0:8]
# res1 = s1.split()
# print (res1)

# suitcase = []
# suitcase.append('полотенце'); suitcase.append('очки'); suitcase.append('кепка'); suitcase.append('шорты'); suitcase.append('книга')
# suitcase.pop()
# suitcase.insert(0, 'ноутбук')
# print (suitcase)

# list_ = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333, ]
# print (list_.count(333))
# print (list_.count(3.1432))
# print (list_.count(86))

# print (list_.index(86))
# list_.pop(5)
# print (list_)

# list_ = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333,]
# list_.sort()
# list_.sort(reverse=True)'abracadabra'
# for i in string:
#     if i == string[6]:
#         string = string.replace(string[5], "K")
# print (string)
# print (list_)
# l1 = [4,3,43,543,4]
# l2 = ['hi', 'hello', 'john']
# l1.append('hello')
# l2.insert(0, 7)
# l1.extend(l2)
# print(l1)

# a = ('b',)
# print(type(a))

# tuple_ = ('a', 1, 'Hello', True, ['1', 'b'])
# tuple_2 = list(tuple_)
# tuple_2.pop(2)
# tuple_3 = tuple(tuple_2)
# print(tuple_3)

# tuple_ = ('b', 1, 'Hello', True, ['False', 'b'], None, ('tuple'))
# print(tuple_[0],tuple_[2], tuple_[4], tuple_[6] )

# print(max(map(int, [_ for _ in input('Введите число: ')])))


# """сравнение списков"""

# numbers1 = [1,2,3,4,5,11]
# numbers2 = [1,2,3,4,5,9,100]

# print (numbers1<numbers2)


# numbers = [2, True, 'Makers', 'hello', ]

# numbers = [2, True, 'Makers', 'hello',(1,2,3)]

# print 

# from random import *
# print (''.join([choice(list ('!@$%^^&*%^&*^%$^&*JFHDSKFNJSDKFGMSDF;OAKLSFNjkdfk;ajhk;sdfjksndf6+5646546541234561321789765454')) for x in range (4)]))
# string = 'abracadabra'
# for i in string:
#     if i == string[6]:
#         string = string.replace(string[5], "K")
# print (string)

print(dir(tuple))