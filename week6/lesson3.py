# Инкапсуляция. getter/setter методы


'''
Инкапсуляция:
    1) Обьеденение всех свойств и методов в одну капслулу или же класс
    2) Ограничение доступа к методам и атрибутам, т.е сокрытие данных от внешнего воздействия




3 модификации доступа:
    public - публичный данные доступны всем
    _protected - защищенный - данные доступны как внутри класса так и у дочерних классов
    __private - приватный - данные доступны только классу в котором он находится
'''

# class A:
#     name = 'John'
#     _age = 30
#     __last_name = 'Snow'

#     def get_name(self):
#         return self.name


#     def _get_age(self):
#         return self._age

#     def __get_last_name(self):
#         return self.__last_name


# class B(A):
#     def get_info(self):
#         print(self.name)
#         print(self._age)
#         print(self.__last_name)
# # obj1 = A()
# # print(obj1.name)
# # print(obj1._age)
# # print(obj1._A__last_name)

# # print(obj1.get_name())
# # print(obj1._get_age())
# # print(obj1._A__get_last_name())


# obj2 = B()
# obj2.get_info()



# Декоратор - меняет\расширяет результат работы (функционал) другой функции


# class Game:
#     __level = 0

#     @property    #getter
#     def level(self):
#         return self.__level

#     @level.setter  #setter
#     def level(self, v):
#         self.__level = v

#     # def get_level(self):             |
#     #     return self.__level          |
      #                                   >  Старый метод
#     # def set_level(self, value):      |
#     #     self.__level = value         |


# obj1 = Game()
# print(obj1.level)
# obj1.level = 5
# print(obj1.level)

# # print(obj1.get_level())
# # obj1.set_level(5)
# # print(obj1.get_level())


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.knowledge = 0

#     def read_book(self):
#         self.__add_point(5)

#     def __add_point(self, point):
#         self.knowledge += point

# obj1 = Student('Nick')
# print(obj1.knowledge)
# # obj1.add_point(100)
# # print(obj1.knowledge)
# obj1.read_book()
# print(obj1.knowledge)

# class A:
#     def __init__(self,name):
#         self.name = name
#     def method1(self):
#         return 'public'
    
#     def _method2(self):
#         return 'protected'
#     def __method3(self):
#         return 'privat'

# obj = A('f')
# print(obj.method1())
# print(obj._method2())
# print(obj._A__method3())


# class A:
#     def method1(self):
#         print('Hello world')

# class B(A):
#     pass

# obj = B()
# obj.method1()

# class Car:
    
#     def __init__(self):
#         self.__speed = 0

#     @property
#     def show_speed(self):
#         return self.__speed

#     @show_speed.setter
#     def set_speed(self, v):
#         self.__speed = v

# bmw = Car()
# bmw.speed = 120
# print(bmw.speed)

# class PrivatProject:
#     __github_link = 'https://replit.com/@Sulaimanovuran/extra-encapsulation#main.py'
#     __developers = ['john@123', 'sam@456', 'nick@789', 'alice@111']
#     def __init__(self, username):
#         self.username = username
#     @property
#     def github_link(self):
#         if self.username in self.__developers:
#             return self.__github_link
#         else:
#             print('Forbidden')

# obj = PrivatProject('nick@789')
# print(obj.github_link)
# obj2 = PrivatProject('jackson@345')
# obj2.github_link




# class User:
#     def _create_user(self):
#         self.email = input()
#         self.password = input()
    
#     def create_user(self):
#         self._create_user()
#         self.is_superuser = False

#     def create_superuser(self):
#         self._create_user()
#         self.is_superuser = True

#     def admin_loggin(self, password):
#         if self.is_superuser == True and password == self.password:
#             print('Successfully logged in')
#         elif self.is_superuser == True and password != self.password:
#             print('Invalid password')
#         else:
#             print('Forbidden')

# obj1 = User()
# obj2 = User()

# obj1.create_user()
# obj2.create_superuser()
# obj1.admin_loggin('password4777')
# obj2.admin_loggin('password')

