#store marks of three subject given by user input


marks={}
x = int(input("enter phy narks :"))
marks.update({"phy" : x})

x = int(input("enter math narks :"))
marks.update({"math" : x})

x = int(input("enter chem narks :"))
marks.update({"chem" : x})

print(marks)