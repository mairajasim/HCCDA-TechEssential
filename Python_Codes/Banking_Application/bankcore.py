#branch_id = 2356
#cust_id = None
#user_info = {}
#def create_account(name, id, psd):
#    pass

#def login(cust_id, psd):
#     pass
# banking_app/bankcore.py

# --- Core Banking Variables ---

# The unique ID for this bank branch.
branch_id = 2057

# This dictionary will store all user information.
# The key is the customer_id, and the value is another dictionary with name and password.
# Example: {'2057-1': {'name': 'Ali', 'password': 'password123'}}
users_info = {}

# A private counter to generate unique user numbers for customer_id.
_user_number_counter = 0


# --- Core Banking Functions ---

def create_account(name, password):
    """
    Registers a new user, generates a unique customer_id, and stores their info.

    Args:
        name (str): The user's full name.
        password (str): The user's chosen password.

    Returns:
        str: The newly generated customer_id for the user.
    """
    global _user_number_counter
    _user_number_counter += 1  # Increment the counter for a new user

    # Generate the unique customer_id using the specified format.
    customer_id = f"{branch_id}-{_user_number_counter}"

    # Store the new user's details in the users_info dictionary.
    users_info[customer_id] = {
        'name': name,
        'password': password
    }

    print(f"Account created successfully! Your Customer ID is: {customer_id}")
    return customer_id


def login(customer_id, password):
    """
    Authenticates a user based on their customer_id and password.

    Args:
        customer_id (str): The user's customer ID.
        password (str): The password provided by the user.

    Returns:
        bool: True if the login is successful, False otherwise.
    """
    # Check if the customer_id exists in our records.
    if customer_id in users_info:
        # If the ID exists, check if the provided password matches the stored one.
        if users_info[customer_id]['password'] == password:
            print(f"Welcome, {users_info[customer_id]['name']}!")
            return True

    # If the customer_id doesn't exist or the password doesn't match.
    print("Invalid login. Please check your Customer ID and password.")
    return False
