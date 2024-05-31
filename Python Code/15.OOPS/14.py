#we can call private methods with help of another methods


class Person:

    def __hello(self):
        print("Hello person!")

    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())