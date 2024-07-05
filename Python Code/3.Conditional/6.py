# Clever if
# <var> = (false_val,true_val) [condition]

sal = float(input("Salary : "))

tax = sal*(0.1, 0.2)[sal <= 50000]

print(tax)
