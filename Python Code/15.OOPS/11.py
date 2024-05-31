#Create Account class with 2 attributes - balance & account no.
#Create methods for debit, credit & printing the balance. Apna College

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    def debit(self,amount):
        self.balance-=amount
        print("Tk.",amount,"was debited")
        print("total balance = ",self.getbalance())
    
    def credit(self,amount):
        self.balance+=amount
        print("Tk.",amount,"was credited")
        print("total balance = ",self.getbalance())

    def getbalance(self):
        return self.balance

acc1=Account(10000,12345)
acc1.debit(500)
acc1.credit(650)