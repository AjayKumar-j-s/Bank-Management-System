from dao.db_connection import DatabaseConnection
from dao.customer_dao import CustomerDAO
from dao.account_dao import AccountDAO
from dao.transaction_dao import TransactionDAO
from controllers.customer_controller import CustomerController
from controllers.account_controller import AccountController
from controllers.transaction_controller import TransactionController
from views.menu_view import MenuView

def main():
    db_connection = DatabaseConnection("bank.db")

    customer_dao = CustomerDAO(db_connection)
    account_dao = AccountDAO(db_connection)
    
    account_controller = AccountController(account_dao)
    customer_controller = CustomerController(customer_dao)
    transaction_dao = TransactionDAO(db_connection)
    transaction_controller = TransactionController(transaction_dao, account_controller)
    menu_view = MenuView(customer_controller, account_controller, transaction_controller)
    
    while True:
        choice = menu_view.display_main_menu()
        
        if choice == 1:
            menu_view.register_customer()
        elif choice == 2:
            menu_view.create_account()
        elif choice == 3:
            menu_view.deposit_money()
        elif choice == 4:
            menu_view.check_balance()
        elif choice == 5:
            menu_view.debit_money()
        elif choice == 6:
            menu_view.view_transaction_history()
        elif choice == 7:
            print("\nBanking Services!")
            break
        else:
            print("\nInvalid choice. Please try again.")
    
    db_connection.close_connection()

if __name__ == "__main__":
    main()
