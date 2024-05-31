#mydict.kyes() -> return all keys


student ={
    "name" : "mehedi",
    "subjects" : {
        "chem" : 78,
        "phy" : 90,
        "math" : 96,
    }
}
#no of keys
print(len(student))
print(student.keys())
#keys ke type cast kore list ba tuples a newa jabe

print(list(student.keys()))
print(len(list(student.keys())))