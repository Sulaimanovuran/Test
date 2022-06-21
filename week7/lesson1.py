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

# class Square:
#   def __init__(self, a, h):
#     self.a = a
#     self.h = h

#   def get_s(self):
#     return self.a * self.h


# class Triangle:
#   def __init__(self, b):
#     self.b = b

#   def get_ss(self, h):
#     return 0.5 * self.b * h


# class Pyramid(Square, Triangle):
#   def __init__(self, a,h):
#     Square.__init__(self, a,h)

#   def get_volume(self, b):
#     v = 1/3 * (self.get_s()) * b
#     return round(v)



# obj = Pyramid(5, 10)
# print(obj.get_volume(6))


#1/3 x основание^2 x высоту



# class Coder:
#   experience = 0
#   count_code_time = 0

#   def get_info(self):
#     return None

#   def coding(self, v):
#     return None



# class Backend(Coder):
#   languages_backend = 'Python'

#   def coding(self, v):
#     self.count_code_time += v
#     return self.count_code_time

#   def get_info(self):
#     return self.languages_backend, self.count_code_time


# class Frontend(Coder):
#   languages_frontend = 'JS'

#   def coding(self, v):
#     self.count_code_time += v
#     return self.count_code_time

#   def get_info(self):
#     return self.languages_frontend, self.count_code_time


# class FullStack(Frontend, Backend):
#   def coding(self, v):
#     self.count_code_time += v
#     return self.count_code_time

#   def get_info(self):
#     return self.languages_frontend,self.languages_backend, self.count_code_time


# dev_py = Backend()
# dev_js = Frontend()
# dev_fs = FullStack()

# dev_py.coding(13)
# dev_py.coding(13)
# print(dev_py.get_info())
# dev_js.coding(8)
# print(dev_js.get_info())
# dev_fs.coding(12)
# print(dev_fs.get_info())




# import time
# class Clock:
#   def get_time(self):
#     time_str = time.strftime('%H:%M:%S')
#     return time_str
    
                        

# class Alarm:
#   def on(self):
#     print('Alarm turn on')
#   def off(self):
#     print('Alarm turn off')

# class AlarmClock(Clock, Alarm):
#   def alarm(self):
#     return self.on()

# obj = AlarmClock()
# obj.alarm()
# print(obj.get_time())
# import math
# class AreaMixin:
#   def area(self,a=0,b=0,c=0,):
#     self.name = input('Введите название фигуры: ')
#     if self.name == 'Куб':
#       return 6 * a**2
#     elif self.name == 'Пирамида':
#       return round(((a**2)*math.sqrt(3)/4)+((3*a/2)*math.sqrt(b *2+a**2/12)))
#     elif self.name == 'Шар':
#       return 4 * math.pi * (a**2)
#     elif self.name == 'Цилиндр': #2 π R h + 2 π R 2
#       return (2 * math.pi * a * b) + (2 * math.pi * a**2)
#     elif self.name == 'Параллелепипед':  # S = 2(a · b + a · h + b · h)
#       return 2 * (a * b + a * c + b * c)


# class Square(AreaMixin):
#   def __init__(self, a, h):
#     self.a = a
#     self.h = h

#   def get_s(self):
#     return self.a * self.h


# class Triangle:
#   def __init__(self, b):
#     self.b = b

#   def get_ss(self, h):
#     return 0.5 * self.b * h


# class Pyramid(Square, Triangle):
#   def __init__(self, a,h):
#     Square.__init__(self, a,h)


# class Cube(Square):
#   def hello(self):
#     print('hello im a cube')



# c = Cube(4,5)
# print(c.area(4))

# p = Pyramid(4,5)
# print(p.area(4,5))

# class CreateMixin:
#   def create(self,dict, k, v):
#     dict[k] = v
#     return dict

# class DeleteMixin:
#   def delete(self, dict, k,):
#     x = dict.pop(k)
#     return f'Удалили задачу: {x}'

# class UpdateMixin:
#   def update(self, dict, v):
#     return dict.update(v)

# class ReadMixin:
#   def sort(self, dict_):
#     sorted_d = sorted(dict_.items(), key =lambda x: x[0])
#     return dict(sorted_d)

  
# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#   todos = {}
#   def __init__(self):
#     pass
#   def set_deadline(self, date):
#     import time
#     x = time.localtime(time.time())
#     res = date - int(x.tm_mday)
#     return res

# o = ToDo()

# o.create(o.todos, 1, "Уборка")
# o.create(o.todos, 4, "Учеба")
# o.create(o.todos, 2, "Работа")
# o.create(o.todos, 3, "Прогулка")

# print(o.todos)

# print(o.delete(o.todos, 1))
# print(o.todos)

# o.update(o.todos,{2:'Тренировка'})
# print(o.todos)

# print(o.sort(o.todos))

# class ExtensionMixin:
#   def add_extension(self, ls, el, nm):
#     ls.append(el)
#     print(f'Добавлено новое расширение {el} для игры {nm}')

#   def remove_extension(self, ls, el, nm):
#     ls.remove(el)
#     print(f'{el} был отключен от {nm}')


# class Game(ExtensionMixin):
#   def __init__(self,game_name,game_type):
#     self.game_type = game_type
#     self.game_name = game_name
#     self.extensions = []

#   def get_description(self):
#     print(f'{self.game_name}-это {self.game_type}')

#   def get_extensions(self):
#     if self.extensions == []:
#       print('No')
#     else:
#       print(self.extensions)


# o = Game('CS', 'шутер от первого лица, в  режиме командного боя')
# o.add_extension(o.extensions, 'gravity', o.game_name)
# o.get_description()
# o.remove_extension(o.extensions, 'gravity', 'CS')
# print(o.extensions)


# x = input()
# list_ = x.split(' ')
# res = list_.sort(reverse = True)
# print(list_[1])