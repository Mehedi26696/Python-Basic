#in place of self we can use different name

class student:
     
    def __init__(self,fullname):
        self.name=fullname
        print("Creating new student...")
    
s1 = student("mehedi")
print(s1.name)
s2 = student("hasan")
print(s2.name)