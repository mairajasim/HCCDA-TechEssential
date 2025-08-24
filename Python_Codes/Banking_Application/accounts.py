# --- Account Data ---

# This dictionary will store the balance for each user.
# The key is the customer_id, and the value is their balance.
# Example: {'2057-1': 5000.0}
balance_record = {}


# --- Account Management Functions ---

def check_balance(customer_id):
    """
    Retrieves and returns the current balance for a given user.

    Args:
        customer_id (str): The customer ID of the user.

    Returns:
        float: The current balance of the user. Returns 0 if user not found.
    """
    # Use .get() to safely retrieve the balance. It returns 0 if the customer_id is not found.
    balance = balance_record.get(customer_id, 0.0)
    return balance


def deposit(customer_id, amount):
    """
    Adds a specified amount to a user's balance.

    Args:
        customer_id (str): The customer ID of the user.
        amount (float): The amount to be deposited. Must be a positive number.

    Returns:
        float: The new balance after the deposit.
    """
    if amount <= 0:
        print("Deposit amount must be positive.")
        return check_balance(customer_id)

    # Get the current balance, or 0 if it's a new account.
    current_balance = balance_record.get(customer_id, 0.0)
    new_balance = current_balance + amount

    # Update the balance in the record.
    balance_record[customer_id] = new_balance
    print(f"Deposit successful. Your new balance is: ${new_balance:,.2f}")
    return new_balance


def withdraw(customer_id, amount):
    """
    Deducts a specified amount from a user's balance if funds are sufficient.

    Args:
        customer_id (str): The customer ID of the user.
        amount (float): The amount to be withdrawn. Must be a positive number.

    Returns:
        float: The new balance after a successful withdrawal.
               Returns the existing balance if withdrawal fails.
    """
    if amount <= 0:
        print("Withdrawal amount must be positive.")
        return check_balance(customer_id)

    current_balance = balance_record.get(customer_id, 0.0)

    # Check if the user has enough funds for the withdrawal.
    if amount > current_balance:
        print("Insufficient balance.")
        return current_balance
    else:
        # If funds are sufficient, deduct the amount.
        new_balance = current_balance - amount
        balance_record[customer_id] = new_balance
        print(f"Withdrawal successful. Your new balance is: ${new_balance:,.2f}")
        return new_balance
