#w+ it's for write and reading 
#it start overwrite full

f = open("test.txt","w+")

f.write("a")
data=f.read()
print(data)