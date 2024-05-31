#Print the elements of the following list using a loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

li=[]
i=1
while i<=10:
    x=i*i
    li.append(x)
    i+=1

j=0
while j<=len(li)-1:
    print(li[j])
    j+=1  