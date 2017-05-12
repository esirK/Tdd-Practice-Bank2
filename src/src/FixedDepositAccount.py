from src.src.Account import Account


class FixedDepositAccount(Account):
    def __init__(self, account_id, account_balance):
        super().__init__(account_id, account_balance)
        self.minimum_deposit = 100

    def check_minimum_balance(self):
        return self.minimum_deposit
