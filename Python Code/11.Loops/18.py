# /*WAP to print reverse of a given
# number.*/

n=int(input("Enter a number : "))
b=0
while(n>1):
    b*=10
    b+=(n%10)
    n=int(n/10)

print(b)

 