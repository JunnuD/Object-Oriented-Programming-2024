class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance
    
    def __str__(self):
        return f"The balance is {round(self.balance, 2)} euros" #Part 1

    def eat_ordinary(self): #Part 2.1
        if self.balance >= 2.95:
            self.balance -= 2.95 
        else:
            print("Insufficient funds for ordinary lunch. ")

    def eat_luxury(self): #Part 2.2
        if self.balance >= 5.90:
            self.balance -= 5.90
        else:
            print("Insufficient funds for luxury lunch. ")

    def deposit_money(self, amount: float): #Part 3
        if amount >= 0:
            self.balance += amount
        else:
            raise ValueError("Deposit must cannot be an negative number")


card = LunchCard(5)
print(card)

card.eat_ordinary()
print(card)

card.eat_luxury()
card.eat_ordinary()
print(card)
card.deposit_money(4000)
print(card)
