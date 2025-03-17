class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f"Account balance: ${self.balance:.2f}")

def main():
    accounts = {}

    while True:
        print("Banking System")
        print("-------------")
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check balance")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            initial_balance = float(input("Enter initial balance: "))
            accounts[account_number] = BankAccount(account_number, initial_balance)
            print("Account created!")

        elif choice == "2":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter amount to deposit: "))
                accounts[account_number].deposit(amount)
            else:
                print("Account not found!")

        elif choice == "3":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found!")

        elif choice == "4":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                accounts[account_number].check_balance()
            else:
                print("Account not found!")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()

class BankAccount:
    def __init__(self, account_number, password, initial_balance=0):
        self.account_number = account_number
        self.password = password
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f"Account balance: ${self.balance:.2f}")

class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = input("Enter account number: ")
        password = input("Enter password: ")
        initial_balance = float(input("Enter initial balance: "))
        self.accounts[account_number] = BankAccount(account_number, password, initial_balance)
        print("Account created!")

    def login(self):
        account_number = input("Enter account number: ")
        password = input("Enter password: ")
        if account_number in self.accounts:
            if self.accounts[account_number].password == password:
                print("Login successful!")
                while True:
                    print("Banking System")
                    print("-------------")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check balance")
                    print("4. Logout")
                    choice = input("Choose an option: ")
                    if choice == "1":
                        amount = float(input("Enter amount to deposit: "))
                        self.accounts[account_number].deposit(amount)
                    elif choice == "2":
                        amount = float(input("Enter amount to withdraw: "))
                        self.accounts[account_number].withdraw(amount)
                    elif choice == "3":
                        self.accounts[account_number].check_balance()
                    elif choice == "4":
                        print("Logout successful!")
                        break
                    else:
                        print("Invalid option. Try again!")
            else:
                print("Incorrect password!")
        else:
            print("Account not found!")

def main():
    bank_system = BankSystem()
    while True:
        print("Banking System")
        print("-------------")
        print("1. Create account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            bank_system.create_account()
        elif choice == "2":
            bank_system.login()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()

import os

class BankAccount:
    #... (remains the same)

class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.config_file = "bank_config.txt"
        self.config_dir = "config"

    def create_account(self):
        #... (remains the same)

    def login(self):
        #... (remains the same)

    def load_config(self):
        if os.path.exists(self.config_dir):
            with open(os.path.join(self.config_dir, self.config_file), "r") as f:
                config_data = f.read()
            # Load the config data into the bank system
            # For example, you could store the config data in a dictionary
            self.config_data = {"bank_name": "My Bank", "bank_address": "123 Main St"}
        else:
            print("Config directory not found!")

    def save_config(self):
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)
        with open(os.path.join(self.config_dir, self.config_file), "w") as f:
            f.write(str(self.config_data))

def main():
    bank_system = BankSystem()
    bank_system.load_config()

    while True:
        #... (remains the same)

    bank_system.save_config()

if __name__ == "__main__":
    main()

import os

# Set the permissions of the config directory
os.chmod(self.config_dir, 0o755)

# Set the permissions of the config file
os.chmod(os.path.join(self.config_dir, self.config_file), 0o644)

if os.access(self.config_dir, os.R_OK):
    # The config directory is readable
else:
    print("Error: config directory is not readable!")

if os.access(os.path.join(self.config_dir, self.config_file), os.R_OK):
    # The config file is readable
else:
    print("Error: config file is not readable!")

import logging
import os

class BankAccount:
    #... (remains the same)

class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.config_file = "bank_config.txt"
        self.config_dir = "config"
        self.log_file = "bank_log.txt"
        self.log_dir = "logs"

        # Set up the logging system
        self.logger = logging.getLogger("BankSystem")
        self.logger.setLevel(logging.INFO)

        # Create a file handler and set the log level to INFO
        file_handler = logging.FileHandler(os.path.join(self.log_dir, self.log_file))
        file_handler.setLevel(logging.INFO)

        # Create a formatter and set the format for the log messages
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        self.logger.addHandler(file_handler)

    def create_account(self):
        #... (remains the same)

        # Log the account creation event
        self.logger.info("Account created for account number %s", account_number)

    def login(self):
        #... (remains the same)

        # Log the login event
        self.logger.info("User logged in with account number %s", account_number)

    def deposit(self, amount):
        #... (remains the same)

        # Log the deposit event
        self.logger.info("Deposited $%.2f into account number %s", amount, account_number)

    def withdraw(self, amount):
        #... (remains the same)

        # Log the withdrawal event
        self.logger.info("Withdrew $%.2f from account number %s", amount, account_number)

    def check_balance(self):
        #... (remains the same)

        # Log the balance check event
        self.logger.info("Checked balance for account number %s", account_number)

    def load_config(self):
        #... (remains the same)

    def save_config(self):
        #... (remains the same)

def main():
    bank_system = BankSystem()
    bank_system.load_config()

    while True:
        #... (remains the same)

    bank_system.save_config()

if __name__ == "__main__":
    main()

import getpass
import hashlib

class BankAccount:
    def __init__(self, account_number, password):
        self.account_number = account_number
        self.password = hashlib.sha256(password.encode()).hexdigest()

    def login(self, password):
        if self.password == hashlib.sha256(password.encode()).hexdigest():
            return True
        else:
            return False

class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = input("Enter account number: ")
        password = getpass.getpass("Enter password: ")
        self.accounts[account_number] = BankAccount(account_number, password)
        print("Account created!")

    def login(self):
        account_number = input("Enter account number: ")
        password = getpass.getpass("Enter password: ")
        if account_number in self.accounts:
            if self.accounts[account_number].login(password):
                print("Login successful!")
                while True:
                    print("Banking System")
                    print("-------------")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check balance")
                    print("4. Logout")
                    choice = input("Choose an option: ")
                    if choice == "1":
                        amount = float(input("Enter amount to deposit: "))
                        self.accounts[account_number].deposit(amount)
                    elif choice == "2":
                        amount = float(input("Enter amount to withdraw: "))
                        self.accounts[account_number].withdraw(amount)
                    elif choice == "3":
                        self.accounts[account_number].check_balance()
                    elif choice == "4":
                        print("Logout successful!")
                        break
                    else:
                        print("Invalid option. Try again!")
            else:
                print("Incorrect password!")
        else:
            print("Account not found!")

def main():
    bank_system = BankSystem()
    while True:
        print("Banking System")
        print("-------------")
        print("1. Create account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            bank_system.create_account()
        elif choice == "2":
            bank_system.login()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()