import unittest

from src.src.Account import Account
from src.src.AccountExistsException import AccountExists
from src.src.Bank import Bank
from src.src.NoAccountException import NoAccount


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_bank_has_no_account_initially(self):
        self.assertEqual(len(self.bank.accounts), 0)
        self.assertDictEqual({}, self.bank.accounts)

    def test_add_account_creates_new_account(self):
        self.bank.add_account(Account('001', 100))
        self.assertEqual(len(self.bank.accounts), 1)
        self.bank.add_account(Account('002', 100))
        self.assertEqual(len(self.bank.accounts), 2)

    def test_bank_can_get_account_balance(self):
        self.bank.add_account(Account('999', 900))
        self.assertEqual(900, self.bank.get_account_balance('999'))

    def test_bank_cannot_get_account_balance_for_non_account(self):
        self.assertEqual(None, self.bank.get_account_balance('1010'))
        self.assertRaises(NoAccount, self.bank.get_account_balance('85858'))

    def test_bank_not_hold_duplicate_accounts(self):
        self.bank.accounts.clear()
        self.bank.add_account(Account('001', 100))
        self.bank.add_account(Account('002', 200))
        account_bal = self.bank.accounts['001']
        self.assertRaises(AccountExists, self.bank.add_account(Account('001', 300)))
        account1_bal = self.bank.accounts['001']
        self.assertEqual(account1_bal, account_bal)
        self.assertEqual(100, account1_bal)
        self.assertEqual(len(self.bank.accounts), 2)

    def test_bank_can_terminate_an_account(self):
        self.bank.add_account(Account('1001', 700))
        self.assertIn('1001', self.bank.accounts.keys())
        self.bank.remove_account('1001')
        self.assertNotIn('1001', self.bank.accounts.keys())

    def test_bank_cannot_terminate_non_existing_account(self):
        accounts_len = len(self.bank.accounts)
        self.assertRaises(NoAccount, self.bank.remove_account('999999999999'))
        self.assertEqual(len(self.bank.accounts), accounts_len)
