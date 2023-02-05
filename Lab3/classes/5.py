class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, a):
        self.balance += a
        print(f"Added {a}KZT to your balance. Your balance is {self.balance}KZT.")
    def withdraw(self, a):
        if a > self.balance:
            print(f"Not enough currence on your balance. Your balance is {self.balance}KZT.")
        else:
            self.balance -= a
            print(f"Withdrawal successful! Your balance is {self.balance}KZT.")
    def status(self):
        print(f"Your balance is {self.balance}KZT.")
p = Account('Abba', 100)
p.deposit(10)
p.withdraw(1000)
p.withdraw(20)
p.status()