class Account:
    def __init__(self,accountType,balance,pin,cash):
        self.accountType=accountType
        self.balance=balance
        self.pin=pin
        self.cash=cash
    def depositCash(self):
        return f"I am going to deposit {self.cash} tomorrow in town"
    def withdrawCash(self):
        return f"I am planning to withdraw {self.balance} for my vaccation next week"