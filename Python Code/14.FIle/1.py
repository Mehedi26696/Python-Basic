# f=open("file_name","mode")
#mode r -> read

f = open("Demo.txt", "r")

data = f.read()
print(data)
print(type(data))
f.close()