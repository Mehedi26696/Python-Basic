#Abstraction
#Hiding the implementation details of a class and only showing the essential features to the user.

class Car:
    def __init__(self):
        self.acc=False   #this info is hidden from user so it's abstraction
        self.brk=False   #this info is hidden from user so it's abstraction
        self.clutch=False #this info is hidden from user so it's abstraction

    def start(self):
        self.clutch=True #this info is hidden from user so it's abstraction
        self.acc=True    #this info is hidden from user so it's abstraction
        print("Car started....")
    
car1 = Car()
car1.start()
