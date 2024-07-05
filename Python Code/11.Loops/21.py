# /*gcd of two numbers*/



a=int(input("Enter a number : "))
b=int(input("Enter a number : "))

if(a>b):
    x=a
    a=b
    b=x
gcd=1
for i in range(1,a+1):
    if(a%i==0 and b%i==0):
        gcd=i
    i+=1

print(gcd)