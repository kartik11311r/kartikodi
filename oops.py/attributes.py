class Account:
    def __init__(self, bal, acc):
        self.balance=bal
        self.account=acc
    #debit method
    def debit(self,amount):
        self.balance=-amount
        print("Rs.",amount,"was debited")

    #credit method
    def credit(self,amount):
        self.balance=+amount
        print("Rs.",amount,"was credited")
    
    #balance
    def get_balance(self):
        return self.balance



acc1=Account(10000,12345)

