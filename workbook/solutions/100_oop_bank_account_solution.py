# Hints:
# - Keep transactions list and methods for deposit/withdraw/transfer; use datetime for timestamps.

# Solution:
from datetime import datetime

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
        self.history = []
    def deposit(self, amt):
        if amt <= 0: raise ValueError('amount must be positive')
        self._balance += amt
        self.history.append((datetime.now(), 'deposit', amt))
    def withdraw(self, amt):
        if amt > self._balance: raise ValueError('insufficient funds')
        self._balance -= amt
        self.history.append((datetime.now(), 'withdraw', amt))
    @property
    def balance(self):
        return self._balance
    def transfer_to(self, other, amt):
        self.withdraw(amt)
        other.deposit(amt)
        self.history.append((datetime.now(), 'transfer_out', amt))
        other.history.append((datetime.now(), 'transfer_in', amt))

# Example
a = Account('Alice', 100)
b = Account('Bob', 50)
a.transfer_to(b, 30)
print(a.balance, b.balance)
print(a.history)
