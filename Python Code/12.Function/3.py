#WAF to print the length of a list. ( list is the parameter)


def l(li):
    idx=0
    for val in li:
        idx+=1
    return idx
nums=[2,4,5,6,7]
print(l(nums))