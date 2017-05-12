import unittest

from src.src.Account import Account


class TestAccount(unittest.TestCase):
    def test_account_object_can_be_created(self):
        account = Account('012', 100)
        self.assertEqual(1, len(account.all_accounts))

    def test_account_returns_current_balance(self):
        account1 = Account('001', 500)
        self.assertEqual(account1.get_balance(), 500)

    def test_every_new_account_is_stored(self):
        a = Account('1020', 900)
        init_accounts = len(a.all_accounts)
        b = Account('909', 100)
        self.assertEqual(init_accounts+1, len(b.all_accounts))

if __name__ == '__main__':
    unittest.main()
