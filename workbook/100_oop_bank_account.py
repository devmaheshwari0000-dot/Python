# Example 100: OOP Project: simple Bank Account system
# Topics: classes, methods, encapsulation, inheritance
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
    def deposit(self, amt):
        if amt <= 0: raise ValueError('amount must be positive')
        self._balance += amt
    def withdraw(self, amt):
        if amt > self._balance: raise ValueError('insufficient funds')
        self._balance -= amt
    @property
    def balance(self):
        return self._balance

class Savings(Account):
    def __init__(self, owner, balance=0, rate=0.01):
        super().__init__(owner, balance)
        self.rate = rate
    def apply_interest(self):
        self._balance += self._balance * self.rate

# Task: extend the system with Transaction history and transfer between accounts
