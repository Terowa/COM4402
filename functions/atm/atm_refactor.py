# atm_refactor.py

"""
Simple ATM refactor – first year level.
Implements the deposit() and withdraw() functions needed by the tests.
"""


def deposit(balance, amount):
    """
    Add amount to balance if amount is positive.

    balance: current balance (number)
    amount: amount to deposit (number, must be > 0)

    Returns the new balance.
    Raises ValueError if amount is not positive.
    """
    if amount <= 0:
        raise ValueError("Deposit amount must be positive")

    return balance + amount


def withdraw(balance, amount):
    """
    Subtract amount from balance if amount is positive and not more than balance.

    balance: current balance (number)
    amount: amount to withdraw (number, must be > 0 and <= balance)

    Returns the new balance.
    Raises ValueError if amount is not positive or is more than balance.
    """
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient funds")

    return balance - amount


def show_balance(balance):
    """
    Return a string showing the current balance to 2 decimal places.

    Example: show_balance(100) -> "Current balance: £100.00"
    """
    return f"Current balance: £{balance:.2f}"

def atm():
    balance = 0.0

    while True:
        print("\n=== Simple ATM ===")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show balance")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            try:
                balance = deposit(balance, amount)
            except ValueError as e:
                print("Error:", e)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            try:
                balance = withdraw(balance, amount)
            except ValueError as e:
                print("Error:", e)
        elif choice == "3":
            print(show_balance(balance))
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

# atm()