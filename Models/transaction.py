class Transaction:
    def __init__(self, account_id, amount, type, transaction_id=None):
        self.id = transaction_id
        self.account_id = account_id
        self.type = type
        self.amount = amount
