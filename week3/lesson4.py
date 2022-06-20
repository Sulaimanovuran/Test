# Введение В Функции. Позиционые и именованные, *args и **kwargs, аргумены по default


# def func1(x,y):
#     return x+y
# print (func1(2,1))


# def func():
#     return 'hello world'
# print(func())

# def func2(str_,num):
#     return str_ * num
# print (func2('hello', 5))

# def func2(str_,num):
#     res = str_ * num
#     return f'Новая строка - {res}'
# print (func2('hello', 5))



# Анотация (Подсказки к аргументам функции и возвращаемому рузультату)

# def func3(num1: int,num2: int) -> int:  
#     return num1 + num2
# print (func3(5,5)) 


#Аргументы по Default (если аргумент не передан он по умолчанию равен указанному значению (1))

# def func4(num1, num2=1):  
#     return num1*num2
# print (func4(3,4))


# def func5(*args):
#     res = 0
#     for i in args:
#         res+=i
#     return res
# print (func5(3,4,3,5,67,8,4))  #94


# def func5(num1, *args):
#     print(num1)  # 3
#     print(args)  # (4, 3, 5, 67, 8, 4)
#     res = 0
#     for i in args:
#         res+=i
#     return res
# print (func5(3,4,3,5,67,8,4)) # 91



# def func6(num1,num2,num3):
#     return num1 // num2 + num3
# print(func6(5,2,3))  # позиционные аргументы
# print (func6(num2=5,num1=2,num3=3))  #именованные аргументы
# print (func6(5, num3=2,num2=3))
# print (func6(num1=5,2,3))  # Error



# def func7(name, age, *args, **kwargs):
#     print (name)
#     print (age)
#     print (args)
#     print (kwargs)
# func7('john', 30, 'Kg', 'bishkek', hobby = 'fishing',age2 = 32)





# def func8 (num1, num2):
#     return num1 + num2
# def func9(num1, num2):
#     return num1 - num2


# def func3():
#     num1 = int(input())
#     num2 = int(input())
#     operator = input()
#     if operator == '+':
#         return func8(num1,num2)
#     elif operator == '-':
#         return (func9(num1,num2))

# while True:
#     answer = input('Хотите продолжить?')
#     if answer == 'Yes':
#         print(func3())
#     else:
# #         break


# def func10(tuple_,*args):
#     res = 0
#     res2 = 0
#     for i in tuple_:
#         res+=i
#     for i in args:
#         res2+=i
#     return res,res2
# print (func10((1,2,3,4),1,2,3,4))


# def my_range(num2,num1,num3):
#     return list(range(num1, num2, num3))
# print (my_range(1,10,2))  #[1, 3, 5, 7, 9]


# def is_even(x: int) -> bool:
#     if x % 2 == 0:
#         return True
#     else:
#         False

# num1 = int(input())
# print (is_even(num1))


# def func(num_start, num_end):
#     res = []
#     for i in range(num_start, num_end):
#         if i % 2 == 0:
#             res.append(i)
#     return res
# print (func(1000, 3001))

# import random
# def func() -> bool:
#     list_ = ['с','в','з','ю']
#     list_1 = random.choices(list_,k = random.randint(1,10))
#     if len(list_1) == 5:
#         return True
#     else:
#         return False
    
# print(func())

# def func(num1,num2):
#   return num1 + num2
# print (func(3,4))

# def func1(str_):
#   return len(str_)
# print (func1('sdjfgasdf'))


# def func2(x,y):
#   res = type(x), type(y)
#   return res
# print(func2('ewrer',54))


# from faulthandler import dump_traceback


# duct_ = {'name':' john', 'age':30}
# print(duct_.keys())


# res=duct_.pop("name")
# print(duct_)
# duct_.setdefault
# print (dir(dict)) 

# for i,j in duct_.items():
#     print (i,j)

# duct_={'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# for k,v in duct_.items():
#     if v % 2 == 0:
#         duct_[k] = 2
#     else:
#         duct_[k] = v
# print(duct_)

# def func4(dict_ = dict):
#     res = []
#     for k in dict_.keys():
#         res+= k
#         return res

    



# def func(dict_):
#     return [key for key in dict_.keys()]
    
# print (func({'name': 'John', 'age': 30}), end=' ')


# def func(num1):
#     if num1 % 2 ==0:
#         return "It's even number"
#     else:
#         return "It's odd number"
# print(func(3))
        

# def func(n1,n2):
#     res = max(n1,n2)
#     return res
# print(func(45,46))


# def func(num):
#     res = 0
#     for i in str(num):
#         res += int(i)
#     return res
# print(func(123))


# def func(list_):
#     res = 1
#     for i in list_:
#         res *= i
# #     return res
#     return res2
# print (func({'name': 'john', 'age': 30}))


# # print (func([1,2,3,4]))


# def func(dict_):
#     res = dict(dict_)
#     res2 = []
#     for k in res.keys():
#         res2 = res2.append(k)
#     return res2
# print (func({'name': 'john', 'age': 30}))



#######  Practice

# def func():
#     print('The function is called')
#     return 'makers'
# print(func())


# def substract():
#     num1 = 20
#     num2 =5
#     print(num1 + num2)
#     return num1 - num2
# substract()

# variable = substract()
# print(variable)


# list_ = [1,2,3,4,5,6,7,9,20,21,22,substract()]
# print(list_)

# def substract():
#     num1 = 20
#     num2 =5
#     print(num1 + num2)
#     return num1 - num2

# def func():
#     print('Im calling substract function')
#     variable = substract()
#     return variable
# print(func())


# def multiplay(a,b):
#     return a / b

# num1 = 70
# num2 = 10
# num3 = 2
# print(multiplay(num1, num2))


# print(num1, num2)


# def welcome(name, last_name):
#     return f'welcome, {name} {last_name}'

# name = input()
# last_name = input()

# print(welcome(name, last_name))

# def get_word(word):
#     list_letters = list(word)
#     return list_letters

# def get_vowels(letters):
#     vowels = ['a','o', 'y', 'i', 'e', 'u']
#     list_vowels =[letter for letter in letters if letter in vowels]
#     res = ''.join(list_vowels)
#     return res


# my_word = input()
# print(get_vowels(get_word(my_word)))


# def info(name = 'sam', age = 19):
#     return f'{name} is {age} years old'

# print (info('john', 39))

# def test_func(n= 1, n2 = 7):
#     return n + n2
# print (test_func(11,2))

# def create_profile(name, age, photo = 'sdfsad.jpg'):
#     return name, age, photo

# print(create_profile(name = 'raychel', age = 30, photo = 'flower.jpg'))

# def func(num):
#     res = 0
#     for i in str(num):
#         res += int(i)
#     return res
# print(func(123))

# def func(word):
#     word_2 = word[::-1]
#     if word == word_2:
#         return True
#     else:
#         return False

# print (func('TNT'))

# def func():
#     n1 = int(input())
#     n2 = int(input())
#     res = max(n1,n2)
#     return res

# print(func())


# def func(num_start, num_end):
#     res = [i for i in range(num_start,num_end) if i % 2 == 0]
#     return res
# print (func(10, 40))

# import random
# def func() -> bool:
#     list_ = ['с','в','з','ю']
#     list_1 = random.choices(list_,k = random.randint(1,10))
#     if len(list_1) == 5:
#         print (list_1)
#         return True
#     else:
#         print(list_1)
#         return False
# print(func())