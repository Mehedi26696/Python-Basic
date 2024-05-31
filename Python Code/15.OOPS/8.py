#Static method
#Methods that don’t use the self parameter (work at class level)

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def hello():
        print("Hello")

    def avg(self):
         sum=0
         for val in self.marks:
            sum+=val
         print("Hi",self.name,"Your avg score is : ",sum/3)

s1 = student("mehedi",[80,70,90])
s1.hello()
s1.avg()


