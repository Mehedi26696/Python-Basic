# /*take input the length and breadth of a rectangle,
# write a program to find whether the area of the
# rectangle is greater than its perimeter*/

l=int(input("Enter the value of length : "))
b=int(input("Enter the value of breadth : "))

if(l*b>(2*(l+b))):
    print("Area is greater")
elif(l*b<(2*(l+b))):
    print("Perimeter is greater")
else:
    print("Both are equal")



 