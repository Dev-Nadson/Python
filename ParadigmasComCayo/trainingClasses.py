class Account:
    def __init__(self, account_number,inital_balance: float):
        self.account_number = account_number
        self.inital_balance = inital_balance
        
    def debit(self, initial_balance, value: float):
        new_balance = initial_balance - value
        return new_balance

    def credit(self, initial_balance, value: float):
        return initial_balance + value

account = Account("202502562756", 500.00)
new_balance = account.debit(account.inital_balance ,20)
account = Account("202502562756", new_balance)
print(account.credit(account.inital_balance ,40))