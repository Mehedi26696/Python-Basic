#r+ it's for write and reading 
#it start overwrite from the begining not full

f = open("test.txt","r+")

f.write("abc")
data=f.read()
print(data)