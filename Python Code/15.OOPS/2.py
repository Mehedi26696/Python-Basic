#Constructor: All classes have a function called __init__(), which is always executed when the object is being initiated.
#*The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
#self and s1 is same

class student:
    name = "Mehedi Hasan"
    def __init__(self):
        print(self)
        print("Creating new student...")
    
s1 = student()
print(s1.name)
print(s1)