

class student:
    college_name= "Dhaka University" #class attributes same for all 
    def __init__(self,name,marks):
        self.name=name  #object attributes
        self.marks=marks
        print("Creating new student...")
    
s1 = student("mehedi",56)
print(s1.name,s1.marks)
print(s1.college_name)
s2 = student("hasan",87)
print(s2.name,s2.marks)
print(s2.college_name)