#with syntax it automatically close the file

with open("Demo.txt","r") as f:
    data =f.read()
    print(data)