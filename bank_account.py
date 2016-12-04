class BankAccount:
    """ Represents a *very simple* bank account with debits and credits."""
    def __init__(self, initial_balance):
        self.balance = [initial_balance]

    def add_withdrawal(self, amount):
        self.balance.append(self.balance[-1] - amount)

    def add_deposit(self, amount):
        self.balance.append(self.balance[-1] + amount)
