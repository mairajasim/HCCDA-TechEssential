#import backcore

#print (f"Enter your Name:{name}")
#psd (f"Enter your password:{psd}")
# banking_app/main.py

# Import the modules from the banking_app package
import bankcore
import accounts

def logged_in_menu(customer_id):
    """
    Displays the menu for a logged-in user and handles their actions.
    """
    while True:
        print("\n--- Logged-In Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")
        choice = input("Please select an option (1-4): ")

        if choice == '1':
            balance = accounts.check_balance(customer_id)
            print(f"Your current balance is: ${balance:,.2f}")

        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: "))
                accounts.deposit(customer_id, amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: "))
                accounts.withdraw(customer_id, amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == '4':
            print("You have been logged out.")
            break # Exit the logged-in loop to go back to the main menu
        else:
            print("Invalid choice. Please select a valid option.")


def main():
    """
    The main function to run the banking application.
    """
    print(">> Welcome to ABC Bank <<")

    while True:
        print("\n--- Main Menu ---")
        print("1. Create a new account")
        print("2. Login to an existing account")
        print("3. Exit")
        choice = input("Please select an option (1-3): ")

        if choice == '1':
            name = input("Enter your full name: ")
            password = input("Create a password: ")
            # Create the account in bankcore
            new_customer_id = bankcore.create_account(name, password)
            # Initialize the balance for the new account in accounts
            accounts.balance_record[new_customer_id] = 0.0

        elif choice == '2':
            customer_id = input("Enter your Customer ID: ")
            password = input("Enter your password: ")
            if bankcore.login(customer_id, password):
                # If login is successful, show the logged-in user menu
                logged_in_menu(customer_id)

        elif choice == '3':
            print("Thank you for using ABC Bank. Goodbye!")
            break # Exit the main application loop
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # This ensures the main function runs only when this script is executed directly
    main()
