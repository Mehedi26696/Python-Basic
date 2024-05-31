#f = open("file_name","w")
#writing mode
#overites the data

f = open("Demo.txt","w")
f.write("I am just a bigginner")

f = open("Demo.txt","r")
data = f.read()
print(data)