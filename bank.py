# from datetime import datetime, time
# now=datetime.now()
# class Account:
#     def __init__(self,name,phone,account,loan_limit) :
#         self.name=name
#         self.phone=phone
#         self.account=account
#         self.balance=0
#         self.loan=0
#         self.loan_limit=loan_limit
#         self.transaction=[]
#         self.repay_loan=[]
#         self.borrow=[]
#         self.withdraw=[]


#     # def show(self,balance):
#     #     return self.balance

#     def deposit(self,amount):
#         if amount <=0:
#             return f"the amount must be grater than zero"
#         else:
#             self.balance +=amount
#             transaction={
#                 "amount":amount,
#                 "balance":self.balance,
#                 "time":now.strftime ("%D"),
#                 "narration":"Deposit"
#                 }
#             self.transaction.append(transaction)
#             return f"dear {self.name} you have deposited KES {amount} your new balance is {self.balance}"

#     def withdraw(self,amount):
#         if amount <=0:
#             return "the amount must be grater than zero"
#         elif (amount<self.balance):
#             return "the amount must be less than the balance"
#         else:
#             self.balance+=amount
#             withdraw={
#                 "amount":amount,
#                 "balance":self.balance,
#                 "time":now.strftime ("%D"),
#                 "narration":"Deposit"
#                 }
#             self.withdraw.append(withdraw)
#             return f"dear {self.name} you have deposited KES {amount} your new balance is {self.balance}"
#     def borrow(self,amount):
#         if amount<=self.loan_limit:
#             return f"you are above your loan limit"
#         elif self.loan>0:
#             return f"you cant borrow loan"
#         else:
#             self.loan+=1
#             self.balance+=amount
#             borrow={
#                 "amount":amount,
#                 "balance":self.balance,
#                 "time":now.strftime ("%D"),
#                 "narration":"Deposit"
#                 }
#             self.borrow.append(borrow)
#             return f"dear {self.name} you have deposited KES {amount} your new balance is {self.balance}"    
#     def get_statement(self):
#         for transaction in self.transaction:
#             narration =transaction["narration"]class Account:
    def __init__(self,phoneNumber, id,name):
         self.phoneNumber=phoneNumber
         self.id=id
         self.name=name
         self.balance=0 
         self.loanLimit=loanLimit
         

    def name(self):
         return f"hello this  is {self.phoneNumber}, {self.id} {self.name}"



    def send(self):
        withdraw=234568
        Send=4567890
        return f"hello this  is {self.withdraw}and{self.send}"


    def show_balance(self):
        return self.balance



    def deposit(self,amount):
        if amount<=0:
            return f"The amount must be greater than zero"
        else:
            self.balance +=amount
            return f" dear {self.amount} you have deposited KES {amount} your new balance is{self.balance}"



    def withdraw(self,amount):
        if amount<=0:
            return f"The amount must be greater than zero"
        elif(amount<self.balance):
            return f"the amount must be less than the balance"
        else:
            self.balance+=amount
            return f"amount reduces the balance"

    def borrow(self,amount):
        if amount<=self.loanLimit:
            return f"you can borrow"
        elif(self.balance<amount):
            return f"you have already an existing loan"
        else:
            self.loan+=1
            self.balance+=amount
            return "you have successfully borrowed"

