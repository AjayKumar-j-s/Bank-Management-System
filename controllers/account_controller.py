from Models.account import Account

class AccountController:
    def __init__(self, account_dao):
        self.account_dao = account_dao
    
    def create_account(self, cust_id, account_type):
        account = Account(cust_id, account_type)
        return self.account_dao.create(account)
    
    def get_balance(self, acc_id):
        account = self.account_dao.find_by_id(acc_id)
        if account:
            return account.balance
        return None
    
    def update_balance(self, acc_id, amount, operation):
        account = self.account_dao.find_by_id(acc_id)
        if not account:
            return False
        
        if operation == "Credit":
            account.balance += amount
        elif operation == "Debit":
            if account.balance < amount:
                return False  
            account.balance -= amount
        
        return self.account_dao.update(account)
    
    def get_account(self, acc_id):
        return self.account_dao.find_by_id(acc_id)
    
    def get_customer_accounts(self, cust_id):
        return self.account_dao.find_by_customer_id(cust_id)
