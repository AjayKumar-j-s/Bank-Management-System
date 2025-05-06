from Models.transaction import Transaction

class TransactionDAO:
    def __init__(self, db_connection):
        self.db_connection = db_connection
    
    def create(self, transaction):
        conn = self.db_connection.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO transactions (account_id, type, amount) VALUES (?, ?, ?)",
            (transaction.account_id, transaction.type, transaction.amount)
        )
        conn.commit()
        
        transaction.id = cursor.lastrowid
        return transaction
    
    def find_by_account_id(self, account_id):
        conn = self.db_connection.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM transactions WHERE account_id = ? ", (account_id,))
        rows = cursor.fetchall()
        
        transactions = []
        for row in rows:
            transactions.append(Transaction(
                row['account_id'],
                row['amount'],
                row['type'],
                row['id']
            ))
        
        return transactions

