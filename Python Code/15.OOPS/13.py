#Private(like) attributes and methods
#Private attributes nd methods are mean to be used only within the class and are not accessible from outside the class
#private-> self.__name

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass #private attributes it's only accessable under scope of class 
    
    def reset_pass(self):
        print(self.__acc_pass) #it's works since it's inside the class


acc1 = Account("12345","abcde")

print(acc1.acc_no)
acc1.reset_pass()
#print(acc1.__acc_pass) #it's give an error since it's outside of the class because it's a private attributes