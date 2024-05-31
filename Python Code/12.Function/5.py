#WAF to find the factorial of n. (n is the parameter)

def fac(n):
    f=1
    for val in range(1,n+1,1):
        f*=val
    return f
x= int(input("Enter a numbeer : "))
print(fac(x))
