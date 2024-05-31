#optional else

st= "University"
for i in st:
    if(i=="r"):
        print("Found")
        break
    print(i)
else:
    print("End")


st= "University"
for i in st:
    if(i=="x"):
        print("Found")
        break
    print(i)
else:
    print("End")