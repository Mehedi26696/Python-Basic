#del keyword

class student:
    def __init__(self,name):
        self.name=name

s1 = student("mehedi")
print(s1)

del s1
print(s1)