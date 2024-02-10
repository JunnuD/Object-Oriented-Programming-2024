class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount: float):
        self.balance += amount
        self.service_charge()

    def withdraw(self, amount: float):
        self.balance -= amount  
        self.service_charge()
    
    def get_balance(self) -> float:
        return self.balance

    def service_charge(self):
        # Calculate the service charge and subtract from balance
        service_charge = self.balance * 0.01
        self.balance -= service_charge

# Test the class
account = BankAccount("Randy Riches", "12345-6789", 3000)

account.withdraw(780)

print(account.account_number)
print(account.owner)

print(account.get_balance())
account.deposit(5000)
print(account.get_balance())
