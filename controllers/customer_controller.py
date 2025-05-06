from Models.customer import Customer

class CustomerController:
    def __init__(self, customer_dao):
        self.customer_dao = customer_dao
    
    def register_customer(self, name, phone, city, state):
        customer = Customer(name, phone, city, state)
        return self.customer_dao.create(customer)
    
    def get_customer(self, cust_id):
        return self.customer_dao.find_by_id(cust_id)
    
    def get_all_customers(self):
        return self.customer_dao.get_all()

