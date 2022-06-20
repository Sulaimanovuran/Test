# Работа с файлами. Json. Import (from)


# Бибилиотека - это набор модулей и функций

# модуль - это файл с расширением .py, который определяет некоторые функции и переменные

# пакет - набор модулей которые упакованы для удобства управления

# встроенные модули math, random, datetime, functools

# from math import pi as PI
# print (PI)

# from math import * # ИМПОРТИРОАТЬ ВСЕ СОДЕРЖИМОЕ

# import my_package
# from test import hello
# print (hello)
# from my_package.test2 import age
# print (age)
# print(my_package.name)


# pi = 1
# print (pi) # 1
# from math import pi
# print (pi) # 3.14564565


######## Файлы

# open()

# file = open('my_files/test1.txt' , 'r')
# print(file.tell()) # 0
# print(file.read())
# print(file.tell()) # 19
# print(file.seek(0)) 
# print(file.read())
# file.close()
# print(file.closed)

# file1 = open('/home/uran/Desktop/py21/week2/file1.txt', 'r')
# print(file1.read())


# file = open('my_files/test1.txt' , 'r')
# print(file.read(5))
# file.close()

# file = open('my_files/test1.txt' , 'r')
# for i in file:
#     print (i)

# file = open('my_files/test1.txt' , 'r')
# print(file.readline())
# print(file.readlines())

# file = open('my_files/test1.txt' , 'r')
# print(file.readline())
# for i in file.readlines():
#     print(i)


# for i in range(3):
#     print (file.readline())

# file = open('my_files/test1.txt' , 'r')
# str_ = file.read()
# str_ = str_.replace('\n', '')
# print (str_)

##### Запись в файл


# file = open('my_files/test2.txt', 'w')

# # file.write('2')
# # for i in range(100):
# #     file.write(str(i) + '\n')
# # file.close() 

# file.write(str(['asd', 'None']))
# file.writelines([ 'asds', 'True'])
# list_ = ['adsd','dfdf', 'sdfsds']

# file.close()

# with open('my_files/test2.txt', 'w') as file:
#     file.write('hello world')


# with open('my_files/test3.txt', 'a') as file:
#     file.write('makers bootcamp ')


# with open('my_files/test2.txt', 'w+') as file:
#     file.write('makers bootcamp ')
#     file.seek(0)
#     print(file.read())

# '''
# r - read
# r+ - read + write
# w - write
# w+ - write + read
# a - append
# a+ - append + read
# x - write
# b - binary
# t - text
# rt -> r
# rb -> rb

# '''
# file1 = open('file.txt', 'r')
# print(file1.read(10)) #Nike: 'Jus
# file1.seek(0)
# print(file1.read(5))
# file1.seek(3)
# print(file1.read(7))

# file1 = open('file.txt', 'r')
# for line in file1:
#     print (line)



# file1 = open('file.txt', 'r')
# list_ = file1.readlines()
# list_ = [line.replace('\n','') for line in list_]
# print (list_)


# file2 = open('bootcamp.txt', 'a')
# print(file2.write('Bootcamp' + '\n'))


# file2 = open('bootcamp.txt', 'w')
# file2.write('Its such a beautiful day today' + '\n')
# file2.write('Todey is my brithday')
# list_mottos = ['just do it', 'Think Different', 
#                 'Got Milk', 'Simple Genius']
# list_mottos = [motto + '\n' for motto in list_mottos]
# print (list_mottos)
# file2.writelines(list_mottos)

# file3 = open('nonfile.txt', 'x')
# list_mottos = ['just do it', 'Think Different', 
#               'Got Milk', 'Simple Genius']
# list_mottos = [motto + '\n' for motto in list_mottos]
# file3.write('Mottos of big companies')
# for motto in list_mottos:
#     file3.write(motto)
# file3.close()
# print(file3.closed)
# with

# with open('nonfile.txt', 'r+') as my_file:
#     print(my_file.read())
#     my_file.write('Additional string')
#     print(my_file.closed)
# print(my_file.closed)

#math, random, datetime


# names = ['john', 'samuel', 'anastasia', 'sherlock']
# names = [x for x in names if len(x)>7]
# print (names)

 


# x,y,z = 7,5,9
# if x>y and x>z:
#     print (x)
# elif y>x and y>z:
#     print (y)
# else:
#     print(z)

# list_ = [1,2,3,4,5,6,7,8,9]
# count_even = 0
# count_odd = 0
# for i in list_:
#     if i % 2 == 0:
#         count_even +=1
#     else:
#         count_odd +=1

# print (f'четные {count_even}, нечетные {count_odd}')


# def func(str_):
#     str_1 = str_[::-1]
#     if str_ == str_1:
#         return True
#     else:
#         return False

# print (func("TNT"))

# list_ = [-1, 2, 3, 0, 5, -3, 7]
# list_ = [True if i > 0 else False for i in list_]
# print(list_)



# with open('my_files/test1.txt', 'r+') as file:
#     print(file.read())
#     file.seek(0)
#     print(len(file.read()))
# with open('my_files/test.txt', 'w') as file:
#     while True:
#         text = input()
#         file.write(text + '\n')
#         if text == '':
#             break


# with open('test2.txt') as file:
#     with open('my_files/test2.txt','w+') as file2:
#         count = sum(1 for line1 in file)
#         file2.write(f'Количество строк: {str(count)} \n')
#         file.seek(0)
#         for line in file:
#             file2.writelines(f'{line} Количество символов: {len(line)}, колчество слов: {len(line.split())} \n')



# with open('my_files/test.txt') as file:
#     print(file.read(9))

# with open('my_files/test.txt', 'r') as f:
#     with open('my_files/test1.txt', 'r+') as f2:
#         for i in f:
#             f2.write(i)
#         f2.seek(0)
#         max_num = max(int(i) for i in f2 if i != '\n')
#         f2.seek(0)
#         min_num = min(int(i) for i in f2 if i != '\n')
#         print(f'Максимальное число {max_num}. Минимальное {min_num}')
#         f2.seek(0)
#         print(f2.read())

    # for i in range(1,16):
    #     f.write(str(i) + '\n')
    #     f.seek(0)
    # max_num = max(int(i) for i in f if i != '\n')
    # f.seek(0)
    # min_num = min(int(i) for i in f if i != '\n')
    # print(max_num,min_num)
    # f.seek(0)
    # print(f.read())
'''
f = open('имяфайла.txt', 'r')
content = f.read()
f.close()
content = content.split("\n")
pupils = []
for line in content:
line = line.split(" ")
pupils.append([line[0], line[1], int(line[2])])
srednia = 0
print("Ниже 3 баллов:")
for p in pupils:
srednia += int(p[2])
if p[2] < 3:
 print(f"{p[0]} {p[1]}: {p[2]}")
srednia /= len(pupils)
print(f"Средняя оценка по классу: {srednia}")
'''

# file = open('test2.txt')
# text = file.read().split('\n')
# file.seek(0)
# students = []
# with open('my_files/test1.txt', 'w') as file2:
#     x = 0
#     score = 0
#     for line in text:
#         line = line.split('.')
#         x += int(line[1])
#     for line in text:
#         line = line.split('.')
#         if int(line[1]) < 3:
#             line = ','.join(line)
#             file2.write(line + '\n')
#     score = x / len(file.readlines())
#     print(f'Средняя оченка класса {round(score)}')
# file.close()

# offices = {
# 1:'google_kazakstan.txt',
# 2:'google_paris.txt',
# 3:'google_poland.txt',
# 4:'google_kyrgyzstan.txt',
# 5:'google_san_francisco.txt',
# 6:'google_germany.txt',
# 7:'google_moscow.txt',
# 8:'google_sweden.txt'
# }
# for k,v in offices.items():
#     print(k,v)
# office = int(input('Введите номер офиса: '))
# text = input('Введите текст: ')
# with open(offices[office],'w+') as file:
#     file.write(text)


def foo():
    var = 'переменная foo'
    print ('переменная в foo: ', var)
  
    def bar():
        global var
        var = 'переменная bar'
 
    bar()
foo()
print('переменная в foo: ', var)

