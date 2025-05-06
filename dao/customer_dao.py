from Models.customer import Customer

class CustomerDAO:
    def __init__(self, db_connection):
        self.db_connection = db_connection
    
    def create(self, customer):
        conn = self.db_connection.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO customers (c_name, ph_no, city, state) VALUES (?, ?, ?, ?)",
            (customer.c_name, customer.ph_no, customer.city, customer.state)
        )
        conn.commit()
        
        customer.c_id = cursor.lastrowid
        return customer
    
    def find_by_id(self, cust_id):
        conn = self.db_connection.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM customers WHERE c_id = ?", (cust_id,))
        row = cursor.fetchone()
        
        if row:
            return Customer(
                row['c_name'],
                row['ph_no'],
                row['city'],
                row['state'],
                row['c_id']
            )
        return None
    
    def update(self, customer):
        conn = self.db_connection.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "UPDATE customers SET c_name = ?, ph_no = ?, city = ?, state = ? WHERE c_id = ?",
            (customer.c_name, customer.ph_no, customer.city, customer.state, customer.c_id)
        )
        conn.commit()
        
        return cursor.rowcount > 0
    
    def get_all(self):
        conn = self.db_connection.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()
        
        customers = []
        for row in rows:
            customers.append(Customer(
                row['c_name'],
                row['ph_no'],
                row['city'],
                row['state'],
                row['c_id']
            ))
        
        return customers
