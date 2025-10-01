class BankAccount:
    def __init__(self, acount_balance=0):
        self.account_balance = acount_balance

    def deposit(self, amount):
        return amount + self.account_balance
    
    def withdraw(self, amount):
        if amount <= self.account_balance:
            return self.account_balance - amount
        else:
            return False
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
    


        
