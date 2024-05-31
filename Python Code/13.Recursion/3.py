#Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    s=n
    if(n==0):
        return 0
    return s+sum(s-1)



x=int(input("Enter a number : "))
print(sum(x))