import unittest

from src.src.Account import Account


class TestAccount(unittest.TestCase):
    def test_account_object_can_be_created(self):
        account = Account('012', 100)

    def test_account_returns_current_balance(self):
        account1 = Account('001', 500)
        self.assertEqual(account1.get_balance(), 500)

if __name__ == '__main__':
    unittest.main()
