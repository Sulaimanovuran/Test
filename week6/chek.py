class Car:
    def __init__(self):
        self.__speed = 0

    def set_speed(self, v):
        self.__speed = v
      
    def show_speed(self):
        return self.__speed

bmw = Car()
bmw.set_speed(150)
print(bmw.show_speed())