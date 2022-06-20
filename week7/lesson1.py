"""
ООП. Наследование: Множественное наследование, Миксины
Проблема ромба
"""

# class Transport:
#   def move(self):
#     return'Этот транспорт:'


# class Boat(Transport):
#   def move(self):
#     return f'{super().move()} Плывет'

# boat = Boat()
# print(boat.move())


# class Call:
#   def call(self):
#     print('call')

# class Mail:
#   def send_letter(self):
#     print('mail')


# class Phone(Call, Mail):
#   pass


# obj1 = Phone()

# obj1.call()
# obj1.send_letter()


# print(Phone.__mro__)



# class Parent1:
#   # def method(self):
#   #   print('Parent1')
#     pass

# class Parent2:
#   # def method(self):
#   #   print('Parent2')
#   pass

# class Child(Parent1, Parent2):
#   # def method(self):
#   #   print('Child')
#   pass


# child = Child()
# child.method()


# class Grandpa:
#   #4) a = 1
#   pass

# class Grandma:
#   #3) a =2
#   pass

# class Dad(Grandma, Grandpa):
#   #2) a = 5
#   pass

# class Mom:
#   # 5) a = 4
#   pass

# class Me(Dad, Mom):
#   # 1) a = 5
#   pass


# p = Me()
# print(p.a) #5, 2, 1, 4


# class A:
#   a =1

# class B(A):
#   a =2

# class C(A):
#   # a = 3
#   pass

# class D(C,B):
#   pass

# o = D()

# print(o.a)
# print(D.__mro__)
  
#________________________________________

# Mixin классы
# Миксины - это особый вид множкственного аследования, глде задача миксинов 
# является расширение функционала других классов(родители классов)


# Работа с Mixin:
  #1) Принято давать имена заканчивающиеся на Mixin (GetterMIxin)
  #2) Mixin не предназначен чтобы от него создавали обьекты
  #3) Нужен чтобы расширить функиционал другого класса

# class MoveMixin:
#   def move(self):
#     print('Двигаюсь')

# class StopMixin:
#   def stop(self):
#     print('Остановился')


# class Person(MoveMixin, StopMixin):
#   pass

# class Car(MoveMixin, StopMixin):
#   pass 


# class AgeMixin:
#   from datetime import time
#   def date(self, age):
#     return f'Привет, вы родились в {2022 - self.age} году'


# class Person(AgeMixin):
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# o = Person('John', 23)
# print(o.date(o.age))