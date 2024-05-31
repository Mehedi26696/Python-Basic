#find factorial of a number

x=int(input("Enter a number : "))
fact=1
for val in range(x,0,-1):
    fact*=val
print(fact)