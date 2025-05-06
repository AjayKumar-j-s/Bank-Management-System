from Models.transaction import Transaction

class TransactionController:
    def __init__(self, transaction_dao, account_controller):
        self.transaction_dao = transaction_dao
        self.account_controller = account_controller
    
    def create_transaction(self, acc_id, amount, transaction_type):
        result = self.account_controller.update_balance(acc_id, amount, transaction_type)
        if not result:
            return None
    
        transaction = Transaction(acc_id, amount, transaction_type)
        return self.transaction_dao.create(transaction)
    
    def get_transaction_history(self, acc_id):
        return self.transaction_dao.find_by_account_id(acc_id)
