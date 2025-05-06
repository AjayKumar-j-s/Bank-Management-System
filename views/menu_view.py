class MenuView:
    def __init__(self, customer_controller, account_controller, transaction_controller):
        self.customer_controller = customer_controller
        self.account_controller = account_controller
        self.transaction_controller = transaction_controller
    
    def display_main_menu(self):
        print("Welcome To Bank Management System")
        print("1. New User - Register Your Details")
        print("2. Create Account")
        print("3. Deposit Money")
        print("4. Check Balance")
        print("5. Debit Money")
        print("6. View Transaction History")
        print("7. Exit")
        
        try:
            choice = int(input("Enter Your Choice: "))
            return choice
        except ValueError:
            print("Please enter a valid number")
            return 0
    
    def register_customer(self):
        print("Customer Registration")
        name = input("Enter Your Name: ")
        phone = input("Enter Your Phone Number: ")
        city = input("Enter Your City: ")
        state = input("Enter Your State: ")
        
        customer = self.customer_controller.register_customer(name, phone, city, state)
        print(f"\nRegistration Completed! Your Customer ID is {customer.c_id}")
    
    def create_account(self):
        print("Create New Account")
        try:
            cust_id = int(input("Enter Your Customer ID: "))
        except ValueError:
            print("Invalid Customer ID format!")
            return
        
        customer = self.customer_controller.get_customer(cust_id)
        if not customer:
            print("Customer not found! Please register first.")
            return
        
        account_type = input("Type of Account To be Created (Savings/Current): ")
        account = self.account_controller.create_account(cust_id, account_type)
        print(f"\nYour Bank Account Successfully Created.Your Account ID is {account.acc_id}")
    
    def deposit_money(self):
        print("Deposit Money")
        try:
            cust_id = int(input("Enter Your Customer ID: "))
            acc_id = int(input("Enter Your Account Number: "))
            amount = int(input("Enter the amount to be deposited: "))
            
            if amount <= 0:
                print("Amount must be positive!")
                return
        except ValueError:
            print("Invalid input format!")
            return
        
        customer = self.customer_controller.get_customer(cust_id)
        if not customer:
            print("Customer not found!")
            return
        
        account = self.account_controller.get_account(acc_id)
        if not account or account.cust_id != cust_id:
            print("Account not found or does not belong to this customer!")
            return
        
        transaction = self.transaction_controller.create_transaction(acc_id, amount, "Credit")
        if transaction:
            print(f"\nAmount {amount} Credited Successfully")
            print(f"New Balance: {self.account_controller.get_balance(acc_id)}")
        else:
            print("Transaction Failed")
    
    def check_balance(self):
        print("Check Balance")
        try:
            cust_id = int(input("Enter Your Customer ID: "))
            acc_id = int(input("Enter Your Account Number: "))
        except ValueError:
            print("Invalid input format!")
            return
        
        customer = self.customer_controller.get_customer(cust_id)
        if not customer:
            print("Customer not found!")
            return
        
        account = self.account_controller.get_account(acc_id)
        if not account or account.cust_id != cust_id:
            print("Account not found or does not belong to this customer!")
            return
        
        balance = self.account_controller.get_balance(acc_id)
        if balance is not None:
            print(f"\nAccount Type: {account.type}")
            print(f"Your Account Balance is {balance}")
        else:
            print("Error retrieving balance")
    
    def debit_money(self):
        print("Withdraw Money")
        try:
            cust_id = int(input("Enter Your Customer ID: "))
            acc_id = int(input("Enter Your Account Number: "))
            amount = int(input("Enter the amount to withdraw: "))
            
            if amount <= 0:
                print("Amount must be positive!")
                return
        except ValueError:
            print("Invalid input format!")
            return
        
        customer = self.customer_controller.get_customer(cust_id)
        if not customer:
            print("Customer not found!")
            return
        
        account = self.account_controller.get_account(acc_id)
        if not account or account.cust_id != cust_id:
            print("Account not found or does not belong to this customer!")
            return
        
        if account.balance < amount:
            print("Insufficient funds!")
            print(f"Current Balance: ${account.balance}")
            return
        
        transaction = self.transaction_controller.create_transaction(acc_id, amount, "Debit")
        if transaction:
            print(f"\nAmount {amount} Debited Successfully")
            print(f"Remaining Balance:{self.account_controller.get_balance(acc_id)}")
        else:
            print("Transaction Failed")
    
    def view_transaction_history(self):
        print("Transaction History")
        try:
            cust_id = int(input("Enter Your Customer ID: "))
        except ValueError:
            print("Invalid Customer ID format!")
            return
        
        customer = self.customer_controller.get_customer(cust_id)
        if not customer:
            print("Customer not found!")
            return
        
        accounts = self.account_controller.get_customer_accounts(cust_id)
        if not accounts:
            print("No accounts found for this customer")
            return
        
        for account in accounts:
            print(f"\nAccount ID: {account.acc_id} (Type: {account.type})")
            print(f"Current Balance: {account.balance}")
            print("Transaction History:")
            print("ID  Type  Amount")
            
            transactions = self.transaction_controller.get_transaction_history(account.acc_id)
            if transactions:
                for transaction in transactions:
                    print(f"{transaction.id} {transaction.type}  {transaction.amount}")
            else:
                print("No transactions found for this account")

