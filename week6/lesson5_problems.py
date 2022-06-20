

# class Employe:
#     count = 0
#     salary = 500

#     def __init__(self,name,surname, pay):
#         self.name = name
#         self.surname = surname
#         self.pay = pay
#         self.email = (name + surname + '@gmail.com').lower()
#         Employe.count += 1


#     def fullname(self):
#         return f'{self.name} {self.surname}'

# obj1 = Employe('John', 'Snow', 500)
# print(obj1.email)
# print(obj1.count)

# obj2 = Employe('John', 'Snow', 500)
# print(obj1.email)
# print(obj1.count)
# print(obj1.fullname())


# class User:
#     def _create_user(self, email, password):
#         self.email = email
#         self.password = password

#     def create_user(self, email, password):
#         self.is_superuser = False
#         self._create_user(email, password)

#     def create_superuser(self, email, password):
#         self.is_superuser = True
#         self._create_user(email, password)

#     def admin_login(self, password):
#         if self.is_superuser and self.password == password:
#             print('Success')
#         elif self.is_superuser == False:
#             print('Forbidden')
#         else:
#             print('invalid password')

        


# user1 = User()
# user2 = User()

# user1.create_superuser('usser123', 'user1')
# user2.create_user('user2244', 'user2')

# user1.admin_login('user1')
# user2.admin_login('user2')



# class User:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     def describe_user(self):
#         print(f'{self.first_name} {self.last_name} {self.age}')

#     def greet_user(self):
#         print(f'Hello {self.first_name}')


# class Admin(User):
#     privileges = [
#     'разрешено добавлять сообщения', 
#     'разрешено удалять пользователей', 
#     'разрешено банить пользователей'
#     ]

#     def show_privileges(self):
#         print(self.privileges)


# obj = Admin('John', 'Snow', 50)
# obj.describe_user()
# obj.greet_user()
# obj.show_privileges()


'''############################ Ассоциация: композиция и агрегация D/Z ##############################'''

# class A:
#     def count_(self, list_):
#         self.list_ = list_
#         res = sum([1 for i in self.list_ if i not in 'ieouay'])
#         return res

# class B(A):
#     def count_(self, list_):
#         self.list_ = list_
#         res = sum([1 for i in list_ if i in 'ieouay'])
#         return res


# obj = A()
# print(obj.count_('sdfgsddfasafqrtuyyu'))

# obj1 = B()
# print(obj1.count_('sdfgsddfasafqrtuyyu'))

# class BaseLift:
#     __floor = 1
#     def __init__(self, max_floor, min_floor = 1):
#         self.max_floor = max_floor
#         self.min_floor = min_floor

#     @property
#     def _floor(self):
#         return  self.__floor

#     @_floor.setter
#     def _floor(self, to_floor):
#         self.__floor = to_floor


# class Lift(BaseLift):
#     def get_floor(self):
#         return self._floor

#     def up(self):
#         if self._floor == self.max_floor:
#             print('NO')
#         else:
#             self.__floor += 1
#             self.get_floor()


#     def down(self):
#         if self._floor == self.min_floor:
#             print('NO')
#         else:
#             self.__floor -= 1
#             self.get_floor()

# lift1 = Lift(15)
# lift1.get_floor()
# lift1.up()
# lift1.up()
# lift1.up()
# lift1.up()


# class WinDoor:
#     def __init__(self, x,y):
#         self.square = x * y

# class Room:
#     def __init__(self, x, y, z):
#         self.square = 2 * z * (x +y)
#         self.wd = []

#     def add_wd(self, w,h):
#         self.wd.append(WinDoor(w,h))

#     def work_surface(self):
#         new_square = self.square
#         for i in self.wd:
#             new_square -= i.square
#         return new_square


# r1 = Room(6,3,2.7)
# print(r1.square)
# r1.add_wd(1,1)
# r1.add_wd(1,1)
# r1.add_wd(1,2)
# print(r1.work_surface())

# with open('nums.txt') as file:
#     n = int(file.readline())
#     for i in range(n):
#         a,b = map(int, file.readline().split())
#         print(a+b)


# def f(a,b):
#     if a % 2 == 0:
#         return a

# a = filter(lambda x: x % 2 == 0, (2,4,5))
# print(list(a))


# from functools import reduce


# print()reduce(lambda a,b: a * b, (89, 12 ,100, 50, 57))