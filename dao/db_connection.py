import sqlite3
import os

class DatabaseConnection:
    def __init__(self, db_name="bank.db"):
        self.db_name = db_name
        self.connection = None
        self.check_and_create_db()
        self.initialize_db()
    
    def check_and_create_db(self):
        if not os.path.exists(self.db_name):
            open(self.db_name, 'w').close()  
            print(f"Database '{self.db_name}' created.")
    
    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_name)
            self.connection.row_factory = sqlite3.Row  
        return self.connection
    
    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None
    
    def initialize_db(self):

        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            c_id INTEGER PRIMARY KEY AUTOINCREMENT,
            c_name VARCHAR(25) NOT NULL,
            ph_no CHAR(10) NOT NULL,
            city VARCHAR(25) NOT NULL,
            state VARCHAR(25) NOT NULL
        )
        ''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            acc_id INTEGER PRIMARY KEY AUTOINCREMENT,
            cust_id INTEGER NOT NULL,
            type VARCHAR(10) NOT NULL,
            balance  INT DEFAULT 0,
            FOREIGN KEY (cust_id) REFERENCES customers (c_id)
        )
        ''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER NOT NULL,
            type VARCHAR(10) NOT NULL,
            amount INT DEFAULT 0,
            FOREIGN KEY (account_id) REFERENCES accounts (acc_id)
        )
        ''')
        
        conn.commit()
        print("Databasetables.") 


