#Search for a number x in this tuple using loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

tup =(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x=int(input("Enter a number : "))

i=0
while i<=len(tup)-1:
    if(tup[i]==x):
        print(i)
    i+=1
