#Print the multiplication table of a number n.

x=int(input("Enter the number :"))
i=1
while i<=10:
    y=i*x
    print(i,"*",x, "=", y)
    i+=1