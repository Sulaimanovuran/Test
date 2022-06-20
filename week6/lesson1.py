# Введение в ООП

# ООП - Обьектно-ориентированное программирование - парадигма (набор правил написания) 
# программирования в котором все основывается на 2 ключевых понтиях класс и обьект


# Класс - Дает общую характеристику их обьекта
# Обьект - экземпляр класса

# class GetInfo:
#     name = 'John'  # Атрибут класса

#     def get_name(self,age):   Cоздание метода
#         print(f'Привет тебя зовут {self.name}, тебе {age} лет')


# obj1 = GetInfo()
# obj1.name = 'Nick'
# obj2 = GetInfo()
# # print(obj1.name)
# # print(obj2.name)

# obj1.get_name(18)
# obj2.get_name(30)

# # len('dfgdfkjg;dfks')  Функция
# # list.append()  Метод


# class Animal():
#     def __init__(self,name,a_type):
#         self.name = name  #Атрибут экземплра класса
#         self.a_type = a_type 
    
#     def get_info(self):
#         return f'Имя обьекта {self.name}, и тип {self.a_type}'


# cat = Animal('Barsik', 'cat')
# print(cat.name)

# dog = Animal('Rex', 'dog')
# print(dog.name)

# print(cat.get_info())
# print(dog.get_info())


# class Person:
#     isalife = True
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#     def get_info(self):
#         return f'{self.name}, {self.last_name}, {self.isalife}'
# john = Person('John', 'Dilinjer')
# Alice = Person('Alice', 'Ogogo')

# print(john.name)
# print(Alice.last_name)
# print(john.isalife)



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def brithday(self):
#         past_age = self.age
#         self.age += 1
#         return f'Тебе было {past_age}, стало {self.age}'


# obj1 = Person('John', 30)

# print(obj1.brithday())
# print(obj1.brithday())

# class Bank:
#     total = 0

#     def get_sum(self):
#         print(self.total)
#     def add_sum(self, sum):
#         self.total += sum
#         self.get_sum()
#     def min_sum(self,sum):
#         if self.total - sum < 0:
#             raise Exception('Недостаточно средств')
#         self.total -= sum
#         self.get_sum()

# client1 = Bank()

# client1.add_sum(1000)
# client1.min_sum(453)
# client1.add_sum(1000)
# client1.min_sum(324)


# class Employe:
#     sum_worker = 0
#     add_cash = 0
#     def __init__(self, name, surname, email, pay):
#         self.name = name
#         self.surname = surname
#         self.email = name + surname + email
#         self.pay = pay
#         Employe.sum_worker += 1
#     def fullname(self):
#         print(f'{self.name} {self.surname}')
#     def add_pay(self, num):
#         self.pay += num


# worker = Employe('John', 'Johnatan','@gmail',1000)
# print(worker.pay)
# print(worker.email)
# worker.fullname()
# worker.add_pay(34)
# print(worker.pay)
# print(worker.add_cash)

# worker2 = Employe('John1', 'Johnatan1','@gmail',1000)
# print(worker2.pay)
# print(worker2.email)
# worker2.fullname()
# worker2.add_pay(34)
# print(worker2.pay)

# print(worker2.sum_worker)

# class Social:
#   type = 'Instagram'
#   count = 0
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#     Social.count += 1
#   def method():
#     return Social.type, Social.count
    

# per1 = Social('John', 23)
# per2 = Social('Alice', 18)
# per3 = Social('Nick', 30)

# print(Social.method())


# class Songs:
#   def __init__(self, name, year, author):
#     self.name = name
#     self.year = year
#     self.author = author
#   def show_title(self):
#       print(f'Эта песня называется "{self.name}"')
#   def show_author(self):
#       print(f'Автор этой песни "{self.author}"')
#   def show_year(self):
#       return f'Эта песня вышла в {self.year} году'

# song1 = Songs('After Hours', '2017', 'The Weekend')
# song1.show_title()
# song1.show_author()
# print(song1.show_year())

# import math
# class Circle:
#   color = 'blue'
#   par  = round(math.pi, 2)
#   def __init__(self, r):
#     self.r = r
#   def area(self):
    
#     S = Circle.par * (self.r ** 2)
#     return round(S)
    

# circle1 = Circle(15)
# circle1.color = 'red'
# print(circle1.par)
# print(circle1.color)
# print(circle1.r)
# print(circle1.area())



# class BankAccount:
#   balance = 0
#   def withdraw(self, amount):
#     self.balance -= amount
#     print(self.balance)
#   def deposit(self, amount):
#     self.balance += amount
#     print(self.balance)


# client1 = BankAccount()
# client1.deposit(122)
# client1.withdraw(45)

# class Taxi:
#   def __init__(self, com_name, boarding, mileage):
#     self.com_name = com_name
#     self.boarding = boarding
#     self.mileage = mileage
#   def cost(self, km):
#     return f'Стоимость посадки  {self.boarding}. Вы проехали {km} км, стоимость поездки {(km * self.mileage) + self.boarding}'


# taxi1 = Taxi('Jorgo', 35, 12)
# print(taxi1.cost(10))
# taxi2 = Taxi('Yandex', 39, 10)
# print(taxi2.cost(10))
# taxi3 = Taxi('Namba', 40, 11)
# print(taxi3.cost(10))
# class PhoneBook:
#   def __init__(self, name, last_name, phone):
#     self.name = name
#     self.last_name = last_name
#     self.phone = phone
#   def get_info(self):
#     print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')
# obj1 = PhoneBook('Samuel','L Jackson',+996708542350)
# obj1.get_info()


# def func(x,y):
#   return x + y


# print(func(34,45))

# class Salary:
#   percent = 8
#   def __init__(self, zp, experience):
#     self.zp = zp
#     self.experience = experience
#   def sum_percent(self):
#     print(self.zp * (self.percent / 100) * (self.experience * 12))

# worker1 = Salary(20000, 5)

# worker1.sum_percent()


# class Nobel:
#   year_now = 2021
#   def __init__(self, category, year, winner):
#     self.category = category
#     self.year = year
#     self.winner = winner
#   def get_year(self):
#     return f'Выиграл {self.year_now - self.year} назад'


# winner1 = Nobel("Литература", 1971, "Пабло Неруда")
# print(winner1.category, winner1.year, winner1.winner)
# print(winner1.get_year())

# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
# print(winner2.category, winner2.year, winner2.winner)
# print(winner2.get_year())

#_______________________________________________________________________
# class Password:
#   def __init__(self, name):
#     self.name = name
#   def __str__(self):
#     return ' '.join(['*' for i in range(len(self.name))])
#   def validate(self):

#     if len(self.name) > 8 and len(self.name)<15 and any([str(x).isdigit() for x in self.name]) and any([str(x).isalpha() for x in self.name]) and any([x for x in self.name if x in '!@#$%^*()']):
#       return 'Ваш пароль сохранен'
#     else:
#       raise Exception('Некорректный пароль')


# p = Password('sdsd27344@')
# print(p.validate())
# print(p)

#--------------------------------------------------------------#
class Pasword:
  def __init__(self,password):
    self.password = password
  def __str__(self):
    return len(self.password) * '*'

  def validate(self):
    list_=['@', '#', '&', '$', '%', '!', '~', '*']
    if not len(self.password) >=8 and  not len(self.password) <= 15:
      raise Exception('Пароль неправильной длины')
    elif self.password.isalpha():
      raise Exception('Добавьте цифры')
    elif self.password.isdigit():
      raise Exception('Добавьте буквы')
    elif not any([i in list_ for i in self.password]):
      raise Exception('You mast added some symbol')
    else:
      print('Good')
    
password1 = Pasword('343h@')
print(password1.validate())
print(password1)



#________________________________________________________________

# class Math():
#   def __init__(self,num):
#     self.num =num
#   def get_factorial(self):
#     factorial =1
#     for i in range(1,self.num+1):
#       factorial*=i
#     return f'Факториал {self.num} = {factorial}'
#   def get_sum(self):
#     from functools import reduce
#     sum =reduce(lambda x,y:int(x)+int(y),list(str(self.num)))
#     return f'сумма цифр = {sum}'
#   def get_mul_table(self):
#      for i in range(11):
#        print(f'{self.num} * {i} = {self.num*i}')


# num1 = Math(11)
# print(num1.get_factorial())
# print(num1.get_sum())
# num1.get_mul_table()


# class  ToDo():
#   todo_list ={}
#   def __init__(self,task): 
#     self.task = task
#   def give_priority(self,priority):
#     self.priority = priority
#     self.todo_list[self.priority]= self.task
#   def list_of_tasks(self):
#     from collections import OrderedDict
#     ordered_by_key = OrderedDict(sorted(self.todo_list.items()))
#     return ordered_by_key

# task10 = ToDo('сходить в кино')
# task10.give_priority(3)
# task11 = ToDo('сходить в душ')
# task11.give_priority(1)
# print(task10.list_of_tasks())