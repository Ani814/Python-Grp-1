"""
ATM Simulator
- Pre‑set balance
- Check balance, deposit, withdraw
- Validation: cannot withdraw more than balance, cannot deposit > 1000 at once
- Logs every operation to atm.log
"""

import logging

# Setup logging
logger = logging.getLogger("atm")
logger.setLevel(logging.INFO)
if not logger.handlers:
    fh = logging.FileHandler("atm.log", encoding="utf-8")
    fh.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
    logger.addHandler(fh)

balance = 5000.0  # initial balance

def log_action(action, amount, new_balance):
    logger.info(f"{action}: {amount} GEL, new balance: {new_balance} GEL")

def check_balance():
    print(f"Your current balance is: {balance:.2f} GEL")

def deposit():
    global balance
    try:
        amount = float(input("Enter amount to deposit (max 1000 GEL): "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        if amount > 1000:
            print("Cannot deposit more than 1000 GEL at once.")
            return
        balance += amount
        print(f"Deposited {amount:.2f} GEL. New balance: {balance:.2f} GEL")
        log_action("Deposit", amount, balance)
    except ValueError:
        print("Invalid amount.")

def withdraw():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        if amount > balance:
            print(f"Insufficient funds. You have {balance:.2f} GEL.")
            return
        balance -= amount
        print(f"Withdrew {amount:.2f} GEL. New balance: {balance:.2f} GEL")
        log_action("Withdraw", amount, balance)
    except ValueError:
        print("Invalid amount.")

def main():
    print("\n===== ATM Machine (GEL) =====")
    while True:
        print("\n1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()