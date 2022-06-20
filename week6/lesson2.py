# Основные принципы ООП: Наследование

# class A:
#     a = 5
#     def get_a(self):
#         print(self.a)
# class B(A):
#     pass

# obj_a = A()
# print(obj_a.a)
# obj_b = B()
# print(obj_b.a)
# obj_b.get_a()

# class Person:
#     def __init__(self, name, last_name, pol):
#         self.name = name
#         self.last_name = last_name
#         self.pol = pol
#     def __str__(self):
#         return self.name
#     def display_name(self):
#         print(f'Name: {self.name}')


# class Employe(Person):
#     def __init__(self, name, last_name, pol, age):
#         super().__init__(name, last_name, pol )
#         self.age = age


# person = Person('john', 'dshfjsakd', 'm')


#     def work(self):
#         print('Я работаю')


# class Student(Person):
#     def study():
#         pass




# person = Person('John')
# print(person)

# employee = Employe('John2')
# print(employee)
# ploye('John2')
# print(employee)



# class A:
#     a =5

#     def info(self):
#         print('hello')

# class B(A):
#     a = A().a + 2
#     def info(self):
#         super().info()
#         print('Hello2')

# a = A()
# b = B()
# # print(a.a)
# # print(b.a)
# a.info()
# b.info()

# class A:
#     def info(self):
#         return 'hello'


# class B(A):
#     def info(self):
#         return super().info() + ' world'

# obj1 = A()
# obj2 = B()

# print(obj1.info())
# print(obj2.info())




# class MyStr(str):
#     def upper(self):
#         return super().upper() + " NO"

# some_str = MyStr('sdfsdfsdf')
# print(some_str.upper())
# print(dir(MyStr))

# class A:
#     pass


# class B(A):
#     pass

# class C(A):
#     pass


# a = A()
# b = B()
# c = C()

# print(isinstance(a, A))
# print(isinstance(b, A))
# print(isinstance(c, A))


# print(issubclass(A, B))
# print(issubclass(B, A))
# print(issubclass(str, A))
# print(issubclass(C, A))



# class Person:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return self.name

# class Employee(Person):
#     def __init__(self, name, company):
#         super().__init__(name)
#         self.company = company
    
#     def __str__(self):
#         return super().__str__() + self.company


# p = Person('John')
# print(p)

# p2 = Employee('Nick', 'Data OX')
# print(p2)


# class Class1:
#   def func1(self):
#     print('hello')
#   def func2(self):
#     print('world')


# class Class2(Class1):
#   def func3(self):
#     print('makers')
#   def func4(self):
#     print('bootcamp')
    
# a = Class2()
# a.func1()
# a.func2()
# a.func3()
# a.func4()

# class A:
#   def method1(self):
#     return 'Основной функционал'


# class B(A):
#   def method1(self):
#     print(super().method1() + ' Дополнительный функционал')

# b = B()
# b.method1()



# class MyString(str):
#     def __init__(self, string):
#         self.string = string
    
#     def __str__(self):
#         return self.string

#     def append(self, word):
#         self.string = super().__str__() + word
#         return self.string

#     def pop(self):
#         res = list(self.string).pop()
#         self.string = self.string[:-1]
#         return str(res)

# b = MyString('hello')
# print(b.string)
# print(b.append(' World'))
# print(b.pop())
# print(b.pop())
# print(b.string)

# print(('sdfsdfsd'.split(',')).pop())


# class A:
#   def method1(self):
#     return 'Основной функционал'


# class B(A):
#   def method1(self):
#     print(super().method1() + ' Дополнительный функционал')

# b = B()
# b.method1()

# class Class1:
#   def func1(self):
#     print('hello')
#   def func2(self):
#     print('world')


# class Class2(Class1):
#   def func3(self):
#     print('makers')
#   def func4(self):
#     print('bootcamp')
    
# a = Class2()
# a.func1()
# a.func2()
# a.func3()
# a.func4()



# class MyDict(dict):
#     def get(self, key, default = None):
#         return super().get(key, 'Are you kidding?')

# dict_ = MyDict({'name':'John', 'age': 23, 'hobby': 'videogame'})
# print(dict_.get('name'))
# print(dict_.get('None'))
# print(dict_.get('city'))
# print(dict_.get('age'))

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def display(self):
#     return f'Имя: {self.name}, Возраст: {self.age}'


# class Student(Person):
#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty
#     def display_student(self):
#         print(f'{self.name}, {self.age}, {self.faculty}')


# person = Person('John', 24)
# print(person.display())

# student = Student('John',24,'medical')
# student.display_student()


# class ContactList(list):
#     def __init__(self, list_):
#         self.list_ = list_

#     def search_by_name(self, name):
#         res = [i for i in self.list_ if i == name]
#         return res

# list1 = ContactList(['john', 'alice', 'sam', 'vin', 'nick', 'john', 'sam', 'aqua', 'west', 'vin'])
# print(list1.search_by_name('sam'))
# print(list1.search_by_name('john'))
# print(list1.search_by_name('aqua'))



# class SmartPhone:
#     batery = 0
#     def __init__(self,name, color, memory):
#         self.name = name
#         self.color = color
#         self.memory = memory

#     def charge(self, add_batery):
#         self.batery += add_batery

#     def __str__(self):
#         return f'{self.name}, {self.batery}'
        

# class Iphone(SmartPhone):
#     def __init__(self,name, color, memory, ios):
#         super().__init__(name, color, memory)
#         self.ios = ios
#     def send_imessage(self, message):
#         print(message, self.name)

# class Samsung(SmartPhone):
#     def __init__(self,name, color, memory, android):
#         super().__init__(name, color, memory)
#         self.android = android
#     def show_time(self):
#         from datetime import datetime
#         current_time = datetime.now().time()
#         print(current_time)
        
# phone = SmartPhone('appel', 'blue', 64)
# phone.charge(45)
# print(phone)
# print(phone.batery)

# samsung12 = Samsung('samsung12', 'blue', 64, 12)
# samsung12.show_time()

# iphone8 = Iphone('Iphone8', 'pink', 128, 10)
# iphone8.send_imessage('hello world')




# 8. Создайте класс Spell для магических заклинаний, экземпляры класса имеют два аттрибута - 
# name - название и formula - полное произношение заклинания. 
# У класса есть два метода: get_description() - дает полное описание заклинания и execute()
#  - совершает заклинание.
# Переопределите у класса метод __str__, чтобы он выдавал вам название, 
# формулу и описание вместе, к примеру:
# Открытие замков: Alohomora
# позволяет магу попасть в любую комнату, 
# способно открыть любую закрытую замочную скважину.
# Наследуя от класса Spell создайте три заклинания,переопределяя в 
# них родительские методы. Создайте объекты этих трех заклинаний. Вызовите все методы

# class Spell:
#     def __init__(self, name, formula):
#         self.name = name
#         self.formula = formula

#     def get_description(self):
#         return 'позволяет магу попасть в любую комнату,\nспособно открыть любую закрытую замочную скважину'

#     def execute(self):
#         print(self.formula)

#     def __str__(self):
#         return f'{self.name}, {self.formula}, {self.get_description()}'


# class Abracadabra(Spell):
#     def __init__(self, name, formula):
#         self.name = name
#         self.formula = formula
#     def get_description(self):
#         return 'Делает все что угодно, только три раза'

#     def execute(self):
#         print(self.formula)

#     def __str__(self):
#         return f'{self.name}, {self.formula}, {self.get_description()}'


# class Sezam(Spell):
#     def __init__(self, name, formula):
#         self.name = name
#         self.formula = formula
#     def get_description(self):
#         return 'Откывает все двери'

#     def execute(self):
#         print(self.formula)

#     def __str__(self):
#         return f'{self.name}, {self.formula}, {self.get_description()}'


# class Shazam(Spell):
#     def __init__(self, name, formula):
#         self.name = name
#         self.formula = formula
#     def get_description(self):
#         return 'Находит любую песню'

#     def execute(self):
#         print(self.formula)

#     def __str__(self):
#         return f'{self.name}, {self.formula}, {self.get_description()}'




# p = Spell('Открытие замков','Alohomora')
# p.get_description()
# p.execute()
# print(p)

# p1 = Abracadabra('Заклинание', 'Abracadabra')
# p1.get_description()
# p1.execute()
# print(p1)


# p2 = Sezam('Open', 'Сезам откройся')
# p2.get_description()
# p2.execute()
# print(p2)

# p3 = Shazam('Find music', 'Shazam')
# p3.get_description()
# p3.execute()
# print(p3)



# class MyCustomError(Exception):
#     def __init__(self, *args):
#         if args:
#             self.message = args[0]
#         else:
#             self.message = None


#     def __str__(self):
#         print('calling str')
#         if self.message:
#             return f'MyCustomError, {self.message}'
#         else:
#             return 'MyCustomError has been raised'

#     def is_upper(self, some_text):
#         if some_text.isupper():
#             print('good')
#         else:
#             raise MyCustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')

# # raise MyCustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')


# p = MyCustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')

# p.is_upper('SDFSDJHJKHJKH')
# import random
# class Character:
    
#     power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }
#     def __init__(self, name):
#         self.name = name
    
#     def give_weapon(self):
#         list_weapon = ['меч', 'пистолет', 'топор', 'лук', 'копье', 'дубина', 'магический посох', 'АК-47']
#         self.weapon = random.choice(list_weapon)
#         return self.weapon
#     def give_role(self):
#         list_role = ["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]
#         self.role = random.choice(list_role)
#     def give_power(self, k,v):
#         self.power_list[k] = v
#         return self.power_list

# class Elf(Character):
#     def __init__(self, name, last_name):
#         super().__init__(name)
#         self.last_name = last_name
    
#     def give_weapon(self):
#         list_weapon = ['меч', 'пистолет', 'топор', 'лук', 'копье', 'дубина', 'магический посох', 'АК-47']
#         self.weapon = random.choice(list_weapon)
#         return self.weapon
#     def give_role(self):
#         list_role = ["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]
#         self.role = random.choice(list_role)
#     def give_power(self, k,v):
#         self.power_list[k] = v
#         return self.power_list


# class Org(Character):
#     def __init__(self, name, high):
#         super().__init__(name)
#         self.high = high
    
#     def give_weapon(self):
#         list_weapon = ['меч', 'пистолет', 'топор', 'лук', 'копье', 'дубина', 'магический посох', 'АК-47']
#         self.weapon = random.choice(list_weapon)
#         return self.weapon
#     def give_role(self):
#         list_role = ["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]
#         self.role = random.choice(list_role)
#     def give_power(self, k,v):
#         self.power_list[k] = v
#         return self.power_list


# class Dragon(Character):
#     def __init__(self, name, head):
#         super().__init__(name)
#         self.head = head
    
#     def give_weapon(self):
#         list_weapon = ['меч', 'пистолет', 'топор', 'лук', 'копье', 'дубина', 'магический посох', 'АК-47']
#         self.weapon = random.choice(list_weapon)
#         return self.weapon
#     def give_role(self):
#         list_role = ["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]
#         self.role = random.choice(list_role)
#     def give_power(self, k,v):
#         self.power_list[k] = v
#         return self.power_list

# p = Character('john')
# print(p.give_weapon())

# elf = Elf('aragon', 'westminster')
# elf.give_weapon()
# elf.give_role()
# elf.give_power('ловкость',10)
# print(elf.power_list)


# org = Org('hren', 198)
# org.give_weapon()
# org.give_role()
# org.give_power('сила', 50)
# print(org.power_list)

# drg = Dragon('gorynych', 3)
# drg.give_weapon()
# drg.give_role()
# drg.give_power('харизма',100)
# print(drg.power_list)


# class User:
#     name = 'John'
#     last_name = 'Snow'
#     def __init__(self, username, email, age):
#         self.username = username
#         self.email = email
#         self.age = age

#     def describe_user(self):
#         return f'Имя: {self.name}, Фамилия: {self.last_name}, Возраст: {self.age}\nНикнейм: {self.username} Эл.почта: {self.email} '
#     def greet_user(self):
#         return f'Здравствуйте {self.name} {self.last_name}'


# class Admin(User):
#     privileges = ['разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить пользователей', 'да']

#     def show_privileges(self):
#         return f'Привелегии пользователя:{self.username}: {self.privileges}'

# user1 = Admin('admin123', 'admin@outlook.com', 23)
# print(user1.describe_user())
# print(user1.greet_user())
# print(user1.show_privileges())

# class House:
#     def __init__(self, house_type, total_area,furniture_list):
#         self.house_type = house_type
#         self.total_area = total_area
#         self.furniture_list = furniture_list
#         self.remaining_area = sum(self.furniture_list.values())
#     def __str__(self):
#         return f'Тип дома: {self.house_type}, общая площадь: {self.total_area}, оставшаяся площадь: {self.total_area- self.remaining_area}, список мебели: {self.furniture_list}'


# my_house = House('townhouse', 150, {'кровать': 4, 'шкаф-купе': 2, 'стол': 1})
# print(my_house)

# line = input()
# n = int(line[0])
# for i in range(n):
#     s = line[i+1].strip()
#     lst = [ord(c) for c in s]
#     nlst = lst[:]
#     nlst.reverse()
    
#     ln = len(s)
#     funny = True
#     for k in range(1, ln):
#         if abs(lst[k]-lst[k-1]) != abs(nlst[k]-nlst[k-1]):
#             funny = False
#             break
            
#     if funny: 
#         print ("Funny")
#     else: 
#         print ("Not Funny")

