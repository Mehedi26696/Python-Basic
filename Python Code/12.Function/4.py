#WAF to print the elements of a list in a single line. ( list is the parameter)
#single line -> end=" "

def l(li):
    for val in li:
        print(val,end=" ")
    
nums=[2,4,5,6,7]
l(nums)
 