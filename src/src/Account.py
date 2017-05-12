class Account(object):
    all_accounts = []

    def __init__(self, account_id, account_balance):
        """
        Initialize a class with its id and initial account balance
        
        :param account_id: 
        :param account_balance: 
        """
        self._account_id = account_id
        self._account_balance = account_balance
        Account.all_accounts.append(self)

    def get_balance(self):
        """
        
        :return: current account balance
        >>> acct = Account('100',100)
        >>> acct.get_balance()
        100
        """
        return self._account_balance

    def get_account_id(self):
        return self._account_id
