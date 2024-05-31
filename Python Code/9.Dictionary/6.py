#dmydict.items() -> returns all (key,val) pairs as tuples

student ={
    "name" : "mehedi",
    "subjects" : {
        "chem" : 78,
        "phy" : 90,
        "math" : 96,
    }
}

print(student.items())
print(list(student.items()))

pairs=list(student.items())
print(pairs[0])