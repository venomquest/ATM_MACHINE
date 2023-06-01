# Sample ATM Machine in Python

# Account data
accounts = {
    '1234567890': {
        'pin': '1234',
        'balance': 5000.0
    },
    '0987654321': {
        'pin': '4321',
        'balance': 10000.0
    }
}

# ATM functions
def authenticate_account():
    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")

    if account_number in accounts and pin == accounts[account_number]['pin']:
        return account_number
    else:
        return None

def check_balance(account_number):
    balance = accounts[account_number]['balance']
    print(f"Your current balance is: ${balance}")

def withdraw(account_number):
    amount = float(input("Enter the amount to withdraw: "))
    if amount <= accounts[account_number]['balance']:
        accounts[account_number]['balance'] -= amount
        print(f"Withdrawal successful. Remaining balance: ${accounts[account_number]['balance']}")
    else:
        print("Insufficient balance.")

def deposit(account_number):
    amount = float(input("Enter the amount to deposit: "))
    accounts[account_number]['balance'] += amount
    print(f"Deposit successful. Current balance: ${accounts[account_number]['balance']}")

# Main ATM loop
while True:
    print("Welcome to the ATM!")
    account_number = authenticate_account()

    if account_number:
        while True:
            print("\nPlease select an option:")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                check_balance(account_number)
            elif choice == '2':
                withdraw(account_number)
            elif choice == '3':
                deposit(account_number)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid account number or PIN. Please try again.")
