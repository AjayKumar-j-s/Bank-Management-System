from Models.account import Account

class AccountDAO:
    def __init__(self, db_connection):
        self.db_connection = db_connection
    
    def create(self, account):
        conn = self.db_connection.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO accounts (cust_id, type, balance) VALUES (?, ?, ?)",
            (account.cust_id, account.type, account.balance)
        )
        conn.commit()
        
        account.acc_id = cursor.lastrowid
        return account
    
    def find_by_id(self, acc_id):
        conn = self.db_connection.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM accounts WHERE acc_id = ?", (acc_id,))
        row = cursor.fetchone()
        
        if row:
            return Account(
                row['cust_id'],
                row['type'],
                row['acc_id'],
                row['balance']
            )
        return None
    
    def find_by_customer_id(self, cust_id):
        conn = self.db_connection.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM accounts WHERE cust_id = ?", (cust_id,))
        rows = cursor.fetchall()
        
        accounts = []
        for row in rows:
            accounts.append(Account(
                row['cust_id'],
                row['type'],
                row['acc_id'],
                row['balance']
            ))
        
        return accounts
    
    def update(self, account):
        conn = self.db_connection.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "UPDATE accounts SET balance = ? WHERE acc_id = ?",
            (account.balance, account.acc_id)
        )
        conn.commit()
        
        return cursor.rowcount > 0