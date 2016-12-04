class BankAccount:
    """ Represents a *very simple* bank account with debits and credits."""
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.balances = [initial_balance]

    def add_withdrawal(self, amount):
        self.balances.append(self.balance - amount)
        self.balance = self.balances[-1]

    def add_deposit(self, amount):
        self.balances.append(self.balance + amount)
        self.balance = self.balances[-1]
