class Account:
    def __init__(self, cust_id, type, acc_id=None, balance=0):
        self.balance = balance
        self.cust_id = cust_id
        self.acc_id = acc_id
        self.type = type
