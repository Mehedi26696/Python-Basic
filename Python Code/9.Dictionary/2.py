#dictionary is unordered
#changeable
#don't allow duplicate keys
info = {
    "name" : "Mehedi",
    "roll" : 13,
    "marks":[23.4,67,24,78],
}
print(info["name"])
print(info["roll"])
print(info["marks"])

info["name"]="hasan"

print(info["name"])
print(info["roll"])
print(info["marks"])

print(info)
print(type(info))
info["new"] ="Football"#new key value pairs assign
print(info)