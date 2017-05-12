from src.src.AccountExistsException import AccountExists
from src.src.NoAccountException import NoAccount


class Bank(object):
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        try:
            if account.get_account_id() in self.accounts.keys():
                raise AccountExists
        except AccountExists:
            print("Account "+account.get_account_id()+" already Exists")
        else:
            self.accounts[account.get_account_id()] = account.get_balance()

    def remove_account(self, account_num):
        return self.chk_account(account_num, 'del')

    def get_account_balance(self, account_num):
            return self.chk_account(account_num, 'return')

    def chk_account(self, account_num, action):
        """
        Checks if an account exists and performs specified action  
        """
        try:
            if account_num not in self.accounts:
                raise NoAccount
        except NoAccount:
            print("No account id "+account_num+" That exists in this bank")
        else:
            if action == 'return':
                return self.accounts[account_num]
            elif action == 'del':
                del self.accounts[account_num]
