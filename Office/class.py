class BankAccount:
    """Represents a basic bank account with common
    operations like deposit, withdraw, balance display."""

    def __init__(self, account_number, account_holder, initial_balance=0):
        """Initilize the new bank account instance"""

        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = initial_balance

    def deposite(self, amount):
        """Deposits funds into the account.the positive amount deposite"""

        if amount > 0:
            self._balance += amount
            print(f"Deposite amount is = {amount}")
        else:
            print("Deposite amount must be positive")

    def withdraw(self, amount):
        """Withdraws funds from the account if sufficient
        balance exists.The positive amount withdraw.
        return True if withdrawal is successfull otherwise False"""

        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdraw amount is= {amount}")
                return True
            else:
                print("Insufficient fund")
                return False
        else:
            print("Withdraw amount must be positive")
            return False

    def display_balance(self):
        """print the current account details balance"""

        print("\n---Account Details---")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self._balance}")


class SavingsAccount(BankAccount):
    """Derived class for savings accounts with an interest rate."""

    def __init__(self, account_number, account_holder,
                 initial_balance=0, interest_rate=0):
        """Initialize the saving account instance"""
        super().__init__(account_number, account_holder, initial_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        """Calculates interest based on the current balance.
        returns the float calculated interest amount"""

        interest = self._balance * self.interest_rate
        print(f"Calculated interest: {interest}.")
        return interest

    def apply_interest(self):
        """Applies the calculated interest to the account balance."""

        interest = self.calculate_interest()
        self.deposite(interest)
        print("Interest applied.", interest)


class CurrentAccount(BankAccount):
    """Represents a current account, inheriting from BankAccount,
     with overdraft capability."""

    def __init__(self, account_number, account_holder,
                 initial_balance=0, overdraft_limit=0):
        """Initialize the current account instance"""

        super().__init__(account_number, account_holder, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """Modifies withdrawal to allow overdrafts
        within the specified limit."""

        if amount <= self._balance:
            return super().withdraw(amount)
        else:
            # Balance insufficient → ask for overdraft
            print("Insufficient balance.")
            choice = input("Do you want to use overdraft? (y/n): ")
            if choice.lower() == 'y':
                if amount <= self._balance + self.overdraft_limit:
                    self._balance -= amount
                    print(f"Withdraw amount = {amount}")
                    print(
                        f"Current balance = {self._balance} (Overdraft used)")
                    return True
                else:
                    print("Overdraft limit exceeded! Withdraw denied.")
                    return False
            else:
                print("Withdraw canceled by user.")
                return False


def savings_account_operations():
    """
    Handles operations for a Savings Account.
    Returns: SavingsAccount: The created savings account object.
    """
    print("-------User input for saving account--------\n")
    # Get user input for account details
    account_number = input("Enter Saving account number=")
    account_holder = input("Enter account holder name=")
    initial_balance = float(input("Enter initial balance for savings="))
    interest_rate = float(input("Enter interest rate="))
    interest_rate = interest_rate / 100

    # ------------Saving account Operations----------------"
    savings = SavingsAccount(account_number, account_holder,
                             initial_balance, interest_rate)

    while True:
        print("\n ------------Saving Account Menu------------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Apply Interest")
        print("4. Display Balance")
        print("5. Exit")

        option = input("\n Select option=")

        if option == "1":
            choice = input("\n Do you want to deposit amount? (y/n):")
            if choice == "y":
                amount = float(input("\n Enter amount to deposit:"))
                savings.deposite(amount)

        elif option == "2":
            choice = input("\n Do you want to withdraw amount? (y/n):")
            if choice == "y":
                amount = float(input("\n Enter amount to withdraw:"))
                savings.withdraw(amount)

        elif option == "3":
            choice = input("\n Do you want to apply interest? (y/n):")
            if choice == "y":
                rate = float(input("Enter interest rate:"))
                savings.interest_rate = rate / 100
                savings.apply_interest()

        elif option == "4":
            savings.display_balance()

        elif option == "5":
            print("\n Existing saving account operation")
            break

        else:
            print("\n Invalid operation please select again")

    return savings


def current_account_operations():
    """
    Handles operations for a Current Account.
    Returns:CurrentAccount: The created current account object.
    """
    print("\n-------User input for current account-----------")
    # Get user input for account details
    account_number = input("\n Enter current account number=")
    account_holder = input("Enter account holder name=")
    initial_balance = float(input("Enter initial balance ="))
    overdraft_limit = float(input("Enter overdraft limit="))

    # -----------Current account opeation-------------"
    current = CurrentAccount(account_number, account_holder,
                             initial_balance, overdraft_limit)

    while True:
        print("\n ----------- Current Account Menu----------")
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Display balance")
        print("4.Exit")

        option = input("\n Select operation:")

        if option == "1":
            choice = input("\n Do you want to Deposit amount? (y/n):")
            if choice == "y":
                amount = float(input("\n Enter amount to deposit="))
                current.deposite(amount)

        elif option == "2":
            choice = input("\nDo you want to withdraw amount? (y/n): ")
            if choice == "y":
                amount = float(input("\nEnter amount to withdraw="))
                current.withdraw(amount)

        elif option == "3":
            current.display_balance()

        elif option == "4":
            print("\n Existing current account operation")
            break

        else:
            print("\n Invalid operation please select again.")

    return current


print("\n====== Account Creation Menu ======")
print("1. Create Savings Account")
print("2. Create Current Account")

choice = input("Enter your choice (1/2): ")

savings = None
current = None

if choice == "1":
    savings = savings_account_operations()

elif choice == "2":
    current = current_account_operations()

else:
    print("Invalid choice")

all_account_data = {}

# Savings account
if savings is not None:
    saving_account_data = {
        "account_type": "Savings",
        "account_number": savings.account_number,
        "account_holder": savings.account_holder,
        "balance": savings._balance,
        "interest_rate": savings.interest_rate
    }
    all_account_data["savings_account"] = saving_account_data

# Current account
if current is not None:
    current_account_data = {
        "account_type": "Current",
        "account_number": current.account_number,
        "account_holder": current.account_holder,
        "balance": current._balance,
        "overdraft_limit": current.overdraft_limit
    }
    all_account_data["current_account"] = current_account_data

# Display all account data
print("\n--------- All Account Data ---------")
print(all_account_data)
