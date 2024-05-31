#mydict.update({"key" : "value"}) -> new key value add hoye jabe dictionary te
 

student ={
    "name" : "mehedi",
    "subjects" : {
        "chem" : 78,
        "phy" : 90,
        "math" : 96,
    }
}

student.update({"city" : "dhaka"})
print(student)

new_dict={"home" : "madaripur", "age" : 18}
student.update(new_dict)
print(student)

n1_dict={"home" : "kalkini", "age" : 18}
student.update(n1_dict)
print(student)