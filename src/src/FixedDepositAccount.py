from src.src.Account import Account


class FixedDepositAccount(Account):
    def __init__(self, account_id, account_balance):
        super().__init__(account_id, account_balance)
        self.minimum_deposit = 100

    def check_minimum_balance(self):
        """
        add doctest
        >>> fda = FixedDepositAccount('001', 300)
        >>> fda.check_minimum_balance()
        100
        :return: 
        """
        return self.minimum_deposit
