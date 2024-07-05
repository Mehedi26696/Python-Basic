#Type of triangles

print("Enter three sides:")
a=int(input())
b=int(input())
c=int(input())
if(a==b and b==c and c==a):
    print("Equilateral Triangle")
elif(a==b or b==c or c==a):
    print("Isosceles Triangle")
elif(a!=b and b!=c and c!=a):
    print("Scalene Triangle")
