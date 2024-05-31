#dict.get("key") ->return value of key

student ={
    "name" : "mehedi",
    "subjects" : {
        "chem" : 78,
        "phy" : 90,
        "math" : 96,
    }
}

print(student["name"])
print(student.get("name"))
#but if write student["name2"] it's return error
# student.get("name2") it's return none

#print(student["name2"])
print(student.get("name2"))