#WAP write a program check if list contain a pallindrome or not

li=[1,2,3,2,1]
new=li.copy()
new.reverse()
if(li==new):
    print("YES")
else:
    print("NO")   