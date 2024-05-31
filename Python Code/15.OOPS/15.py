#Inheritance
#When one class(child/derived) derives the properties and methods of another class(parent/base)

class Car:
    @staticmethod
    def start():
        print("car started.....")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

class Fortuner(ToyotaCar):
    def __init__(self, brand):
        self.brand=brand

car1 = Fortuner("diesel")
car1.start()
