# /*Take positive integer input and tell if it
# is divisible by 5 and 3.*/


n=int(input("Enter a positive number : "))
if(n%5==0 and n%3==0):
    print("Divisible")
else:
    print("Not Divisible")