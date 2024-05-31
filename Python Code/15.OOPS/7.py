#Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average.


class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
         sum=0
         for val in self.marks:
            sum+=val
         print("Hi",self.name,"Your avg score is : ",sum/3)

s1 = student("mehedi",[80,70,90])
s1.avg()
