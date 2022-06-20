#Множество (set()) - это изменяемый, неупорядоченный и итерируемый тип данных.


# {} - литералы
# set_ = {}
# print (type(set_))
# set_ = {1,2,3,4}
# dict_= {'a': 'kfnsamn'}

# set_ = {1,2,3,4,'d','sf', 4, 3, 2, 1}
# print (set_)

# set_ = {[1,2,3], [2]} # Eror не может хранить изменяемый тип данных
# set_ = {(1,2,3), (3)} # Только неизиеняемый (приммер : кортеж)

# res = [1,2,3,3,2,2,3,2,222,3,2,221,1,1,1,1]
# print (set(res)) #{1, 2, 3, 221, 222} удаляет дублирующиеся значения


# l = [1,2,3,4,5,10,]
# fl = []
# for i in l:
#     f = 1
#     for j in range (1 ,i+1):
#         f *= j
#     fl.append(f)
# print (fl)

# for i in range(5):
#     if  i == 2:
#         break
#     print (i)
#     else: # не сработает если встретит break

# for i in range(11):
#     print ('Четное') if i % 2 == 0 else print ('Нечетное')
#     # if i % 2:
#     #     print ('Четные')    # ВЫВОДИ НЕЧЕТНЫЕ ЧИСЛА
    # else:
    #     print ('Нечетные')


# text_ ='sdjfjdfnajnanjnfaajfnajdnfajfnjdnajdnjsdweoioq,x   qwpoz,jnewjf'

# while True:
#     word = input()
#     print (text_.count(word))

# СОЖИТЬ ЦИФРЫ ЧИСЛА


# num = int(input())
# s = 0
# for i in str(num):
#     s += int(i)
# print (s)
 

# НАЙТИ ПОЛИНДРОМ


# list_ = [55,56, 'hello', 'aba', 'c', 'lol']
# for i in list_:
#     if str(i) == str(i)[::-1]:
#         print ('yes')
#     else:
#         print ('no')


# import random

# num = int(input())
# range_ = random.randint(0, 10)
# try_ = 3

# while True:
#     num2 = int(input())
#     if num2 == num:
#         print(f'uuuuuuuu {num}')
#         break
#     else:
#         try_ = try_ - 1
#         print (f'try {try_}')
#     if try_ == 0:
#         print ("end")
#         break


# import random
# l = []
# for i in range(101):
#     l.append(random.randint(-10, 10))
# print(len(l) - len(set(l)))


# import os
# os.system('ls')   # задавать команды ОС

# res = []
# for i in range(1,11):
#     for j in range(1,11):
#         res = i * j

#         print (f'{i} * {j} = {res}')


# res = []
# lst_ = ['hello']
# word = lst_[0]
# if len(word) % 2 != 0:
#     res.extend(list(word[len(word)//2+1:]))
#     res.extend(list(word[:len(word)//2+1]))
# else:
#     res.extend(list(word[len(word)//2+1:]))
#     res.extend(list(word[:len(word)//2+1]))
# print (res)


# for i in range (1, 100):
#     if i % 3 == 0 and i % 5 == 0:
#         print ('fizz')
#     elif i % 3 == 0:
#         print ('fizzbuzz')
#     elif i % 5 == 0:
#         print ('buzz')

# факториал чисел от (0 - 20) двумя способами while и for

