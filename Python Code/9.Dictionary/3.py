#nested dictionary

student ={
    "name" : "mehedi",
    "subjects" : {
        "chem" : 78,
        "phy" : 90,
        "math" : 96,
    }
}

print(student)
print(student["subjects"])

print(student["subjects"]["phy"])