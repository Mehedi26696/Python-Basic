# /*WAP to sum of digits of a given number.*/

n=int(input("Enter a number : "))

sum=0
while(n>1):
    sum+=(n%10)
    n=int(n/10)

print(sum)
