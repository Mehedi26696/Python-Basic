# /*WAP to check if a number is prime or
# not.*/

 
n=int(input("Enter a positive number : "))
flag=False
for i in range(2,n):
    if(n%i==0):
        flag=True
    i+=1

if(flag==True):
    print("Not prime")
else:
    print("Prime")


