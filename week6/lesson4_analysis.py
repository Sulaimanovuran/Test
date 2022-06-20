# Повтор тем

# class MyStr(str):
#     pass
#     def __str__(self):
#         return super().__str__() + ' world'

# obj1 = MyStr('hello')
# print(obj1)

# class A:
#     name = 'John'
#     def __init__(self, name, last_name):
#         self.name = name 
#         self.last_name = last_name

# class B(A):
#     def __init__(self, name, last_name, age):
#         super().__init__(name, last_name)
#         self.age = age

# b = B('John', 'Snow', 67)

# print(dir(b))


# class Game():
#     __level = 0


#     def play_game(self, hours):
#         if hours > 2:
#             self.__level += 1

#     @property
#     def level(self):
#         return self.__level

#     @level.setter
#     def l(self, value):
#         self.__level = value


# john = Game()
# john.play_game(3)
# john.play_game(3)
# john.l = 100

# print(john.level)


# class Soda:
#     def __init__(self, value):
#         if isinstance(value, str)
#         # if value != str(value):
#         #     self.v = None
#         else:
#             self.v = value


# obj = Soda('asdfsf')
# obj2 = Soda(233)

# print(obj.v)
# print(obj2.v)


# class KgToPounds:
    
#     def __init__(self, kg):
#         self.__kg = kg

#     @property
#     def get_kg(self):
#         return self.__kg

#     @get_kg.setter
#     def set_kg(self, new_kg):
#         self.__kg = new_kg


# obj = KgToPounds(14)
# obj.set_kg = 15
# print(obj.get_kg)