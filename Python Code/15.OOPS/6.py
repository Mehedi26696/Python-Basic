#method Methods are functions that belong to objects.

class student:
     
    def __init__(self,name,marks):
        self.name=name  
        self.marks=marks
    def welcome(self):
        print("Welcome student",self.name)   
    def get_marks(self):
        return self.marks


s1 = student("mehedi",56)
s1.welcome()
print(s1.get_marks())