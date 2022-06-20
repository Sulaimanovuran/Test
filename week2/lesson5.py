# Разбор тем

# list список
# arrays массив


#Python динамически типизированный тип данных, (можно менять тип данных)

# some_list = [1,2,3, 'hello'] список

# int some_list = [1,2,3,4,5] массив хранит только один тип данных

# str_ = 'helloworld'
# print(str_ + 'some text') helloworldsome text   Строка неизменяемый тип данных
# print (str_) hello world

# ls = ['audi']
# print ('before', ls)
# ls.append('toyota')
# print ('after', ls)


# LIFO = Last in First Out
# FIFO = First in First Out


# ls = ['aidi', 'toyota', 'mercedes', 'bmw']
# print ('before', ls)
# removed = ls.pop(0)
# print (removed)
# print ('after', ls)

# ls = ['aidi', 'toyota', 'mercedes','aidi','bmw']
# ls.remove('aidi')
# print (ls)


# phone_numbers = [999,222,555,111,666,333,999,777,888,111,222]
# unique_phine_numbers = []
# for number in phone_numbers:
#     if number not in unique_phine_numbers:
#         unique_phine_numbers.append(number)
#     else:
#         continue
# print (unique_phine_numbers)


# phone_numbers = [999,222,555,111,666,333,999,777,888,111,222]
# phone_numbers.insert(215 110)
# print (phone_numbers)


# print(dir([]))


# string = ['hello', ' world', 'fir','if']
# string.sort(key=len)
# print(string)


# ls_original = ['john', 'rauchel', 'peter', 'jessica',['test1','test2']]
# cp_ls = ls_original.copy()
# cp_ls[4][0] = 'arnold'
# print (cp_ls) #['john', 'rauchel', 'peter', 'jessica', ['arnold', 'test2']]
# print (ls_original)  #['john', 'rauchel', 'peter', 'jessica', ['arnold', 'test2']]
# # ПОВЕРХНОСТНОЕ КОПИРОВАНИЕ ИЗМЕНЯЕТ СПИСОК

# import copy

# ls_original = ['john', 'rauchel', 'peter', 'jessica',['test1','test2']]
# cp_ls = copy.deepcopy(ls_original)
# cp_ls[4][0] = 'arnold'
# print (cp_ls)   #['john', 'rauchel', 'peter', 'jessica', ['arnold', 'test2']]   
# print (ls_original) #['john', 'rauchel', 'peter', 'jessica', ['test1', 'test2']]
# ГЛУБОКОЕ КОПИРОВАНИЕ СОХРАНЯЕТ ИСХОДНОЕ ЗНАЧЕНИЕ



# генерация пароля 

# import string
# import random

# password = ''
# for _ in range(2):
#     password +=random.choice(string.ascii_uppercase)
# password +=random.choice(string.digits)
# password +=random.choice(string.punctuation)

# ls = list(password)
# random.shuffle(ls)
# print (''.join(ls))


# как определить тип метода
# ''.join()  еслт он принимает списки содержашие строки то это метод строк ("") ---- идентиикатор

# udemi.com/ mycourses

# xx = 15
# if True:
#     xx = 20
# print (xx)

# names = ['john', 'sam', 'alice', 'bob', 'harry']
# for name in names:
#   print (name)

# numbers = [1,32,43345,3234,344,34,65,34]
# num1 = []
# num2 = []
# for i in numbers:
#   if i % 2 == 0:
#     num1.append(i)
#   else:
#     num2.append(i)
# print (num1, num2)

numbers1 = [1,2,3,4,5]
numbers2 = [23,455,67,44]
numbers1.extend(numbers2)
sum(numbers1)