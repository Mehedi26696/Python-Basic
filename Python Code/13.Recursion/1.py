#recursion
#print n to 1

def nums(a):
    if(a==0):# base case
        return
    print(a)
    nums(a-1)
x=int(input("Enter a number : "))
nums(x)