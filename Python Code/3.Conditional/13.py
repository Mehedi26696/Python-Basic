# /*Take 3 numbers input and tell if they
# can be the sides of a triangle.*/

print("Enter three sides of a triangle")
a=int(input())
b=int(input())
c=int(input())

if(a+b>c):
    if(b+c>a):
        if(c+a>b):
            print("Can be a triangle")
else:
    print("Can't be a triangle")
    
 