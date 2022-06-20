# def func(*args,a=5,b=10):
#     print (a,b,args)
# func(7,a=2,b=3)


# # is ==
# l1 = [1,2,3]
# l2 = [1,2,3]

# print (id(l1))
# print (id(l2))

# print (l1 == l2) # True, сравнение по значению
# print(l1 is l2) # False, сравнение по id

# l1 = [1,2,3,[5,6]]
# l2 = l1
# print(l1) #[1, 2, 3, [5, 6]]
# print(l2) #[1, 2, 3, [5, 6]]
# l1.pop()
# print (l1) #[1, 2, 3]
# print (l2) #[1, 2, 3]


# l1 = [1,2,3,[5,6]]
# l2 = l1.copy()
# l1[0]='hello'
# l1[-1][0]= 'world'
# print (id(l1[-1]))
# print (id(l2[-1]))


# import this
'''
1) Обявление 
    1) глагол
    2) sake case
    3) () - обязательны
    4) параметры не обязательно
2) Тело функции
    1) 4 пробела
    2) return (если не напишем то будет - None)
    3) внутри тела функции можно писать любой код
3) Single Reponsibility - принцип единой ответсвенности
 (функция должна отвечать только за одну логику)
4) Аргументы:
    Есть 2: позиционные и именованные
5) Есть понятие значения по дефолту(по умолчанию)
6) *args, **kwargs
7) def func(a,b): параметры
    pass
    func(a,b)  аргументы
8) Аннотация

'''
# def some_name():
#     pass

# def func(a=5, b=3):
#     print(a,b)
# func()
# func(b=6, a = 7)
# func(5,7)
# func(6,b=5)


# def func(*args):
#     res = None
#     res = args[0] if args[0]>args[1] else args[1]
# print(func(4,7))



# def func1():
#     a = 4
#     def inner():
#         a += 2
#     return a
# print (func1())

# def func2():
#     a=4
#     def inner(var):
#         var+=1 
#         return var
#     return inner(a)
# print(func2())


# lambda - анонимная функция


# def func1(x,y):
#     return x+y

# func1_1 = lambda x,y: x + y

# print (func1_1(2,2))


# func2 = lambda x,y: x if x> y else y
# print (func2(7,4))


# def func(words: list):
#     '''Эта функция которая поверяет вляется ли слово палиндромом'''
#     a =[]
#     for i in words:
#         if str(i) == str(i)[::-1]:
#             a.append('Yes')
#         else:
#             a.append('No')
#     return a
# print(func(['hello', 5, 'aba', 'aa', 'world']))


from unittest import expectedFailure


# def validate_email(email: str):
#     '''functions for validate email'''
#     domains = ['gmail.com', 'mail.ru']
#     index = email.find('@')
#     print (index)
#     if '@' not in  email:
#         raise Exception ('Invalid email')
#     elif email[index+1:] not in domains:
#         raise Exception ('Invalid domain')
    
#     return True

# email = input()
# print (validate_email(email))