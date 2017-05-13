import unittest

from src.src.Account import Account
from src.src.FixedDepositAccount import FixedDepositAccount


class TestFixedAccount(unittest.TestCase):
    def setUp(self):
        initial_account = Account('001', 100)
        self.inti_size = len(initial_account.all_accounts)

    def test_fixed_account_is_added_to_list_of_all_other_accounts(self):
        fixed_account = FixedDepositAccount('002', 100)
        self.assertEqual(self.inti_size+1, len(fixed_account.all_accounts))

if __name__ == '__main__':
    unittest.main()
