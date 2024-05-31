#slicing also possible in list
#syntex li[strting_idx : ending_idx] #ending idx not included
#li[0 : 4] and li[ : 4] is same
#li[4: ] and li[4 : len(li)] is same


li=[3,67,89,90,45,23,46,32]


print(li[1 : 5])
print(li[ : 5])
print(li[5 : ])

print(li[-4 : -1])
print(li[-4 : ])
print(li[-len(li) : ])