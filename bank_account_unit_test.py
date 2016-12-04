import unittest
from bank_account import BankAccount

class BankAccountTest(unittest.TestCase):
    def setUp(self):
        self.bank_account = BankAccount(100)

    def test_deposit(self):
        self.bank_account.add_deposit(100)
        self.assertEqual(200, self.bank_account.balance)

    def test_withdrawal(self):
        self.bank_account.add_withdrawal(100)
        self.assertEqual(0, self.bank_account.balance)
