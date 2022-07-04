"""
Полиморфизм - возможность использовать один и тот же метод для 
разных классов, при этом результат может меняться в зависимости от того
к какому классу принадлежит обьект


Полиморфизм - множество форм
"""

# def add(x,y):
#     return x + y
    
# print(add(5,5))
# print(add('5', '5'))


# print(len('python'))
# print(len([1,2,3,4,5]))
# print(len({'a':8}))


# class Cat:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#     def make_sound(self):
#         return 'Meoww'


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def make_sound(self):
#         return 'Gav'

# cat = Cat('Barsik', 10)
# dog = Dog('Rex', 8)

# print(cat.make_sound())
# print(dog.make_sound())

# list_ = [cat, dog]

# for i in list_:
#     print(i.make_sound())


# from math import pi

# class ShapeMixin:
#     '''Класс для описания форм'''
#     def __init__(self, name):
#         self.name = name
#     def __str__(self) -> str:
#         return self.name

# class Square(ShapeMixin):
#     def __init__(self, lenght):
#         super().__init__('Square') 
#         self.lenght = lenght

#     def area(self):
#         return self.lenght ** 2

# class Circle(ShapeMixin):
#     def __init__(self, radius):
#         super().__init__('Circle')
#         self.radius = radius

#     def area(self):
#         return self.radius **2 * pi



# square1 = Square(4)
# square2 = Square(2)

# circle1 = Circle(10)
# circle2 = Circle(5)

# list_ = [square1, square2, circle1, circle2]
# for i in list_:
#     print(i.area())

# [print(i.area()) for i in list_]


'''
Абстракция - абстрактный класс опредеялет общий интерфейс для набора подклассов
Заставляя дочерние классы рефлизовывать абстрактные методы
'''


# from abc import ABC, abstractclassmethod
# class A(ABC):
#     def method1(self):
#         pass
#     @abstractclassmethod
#     def method2(self):
#         pass

# class B(A):
#     def method2(self):
#         pass

# b = B()

# from abc import ABC, abstractclassmethod
# class Peaople(ABC):
#     @abstractclassmethod
#     def breathe(self):
#         pass
#     @abstractclassmethod
#     def eat(self):
#         pass
#     @abstractclassmethod
#     def move(self):
#         pass
#     @abstractclassmethod
#     def sleep(self):
#         pass


# class Person(Peaople):
#     def breathe(self):
#         print('я умею дышать')
#     def sleep(self):
#         print('я умею дышать')
#     def eat(self):
#         print('я умею есть')
#     def move(self):
#         print('я умею ходить')

# obj = Person()


# class Animals(ABC):
#     @abstractclassmethod
#     def method1(self):
#         pass
#     def method2(self):
#         print('я')


# class Cat(Animals):
#     def __init__(self, name):
#         self.name= name

#     def method1(self):
#         print(f'im a cat')

#     def method2(self):
#         print(f'my name is {self.name}')

# class Dog(Animals):
#     def __init__(self, name):
#         self.name = name

#     def method1(self):
#         print('im a dog')

#     def method2(self):
#         print(f'my name is {self.name}')

# list_ = range(1,100)
# for i in list_:
#     if i % 3 == 0 and i % 5 == 0:
#         print('fizzbuzz')
#     elif i % 3 == 0:
#         print('fizz')
#     elif i % 5 == 0:
#         print('buzz')

# x,y,z = 'John', [1,2,3,4], {'name': 'Eddard', 'last_name':'Stark'}
# list_= [x,y,z]
# list1 = [len(i) for i in list_]
# print(list1)


# class Dog:
#     def voice(self):
#         print('гав')
    
# class Cat:
#     def voice(self):
#         print('мяу')

# cat = Cat()
# dog = Dog()

# def func(animal):
#     return animal.voice()

# func(cat)
# func(dog)



# class Solution:
#     def longestCommonPrefix(self, strs):
#          if len(strs) == 0:
#             return ''
#          s = strs[0]
#          for i in range(1, len(strs)):
#             while strs[i].find(s) != 0 :
#                 s = s[:-1]
#          return s

# s = "()[]{}"
# print(round(len(s) / 2))
# print(s[round(len(s) /2):] == s[round(len(s) /2)-1::-1])
