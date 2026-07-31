class BankAccount:
    bank_name = "State Bank of India"
    total_accounts = 0
    interest_rate = 4.0
    MIN_BALANCE = 500
    _next_account_number = 1001

    def __init__(self, holder_name, account_type, initial_deposit, pin):
        """Initialize a bank account."""
        if initial_deposit < BankAccount.MIN_BALANCE:
            raise ValueError(
                f"Opening deposit must be at least {BankAccount.MIN_BALANCE}"
            )

        if not isinstance(pin, str) or len(pin) != 4 or not pin.isdigit():
            raise ValueError("PIN must be exactly 4 digits")

        self.holder_name = holder_name
        self._account_number = BankAccount._next_account_number
        self._account_type = account_type
        self.__balance = initial_deposit
        self.__pin = pin

        BankAccount._next_account_number += 1
        BankAccount.total_accounts += 1

    @property
    def account_number(self):
        """Return the account number."""
        return self._account_number

    # balance must be read-only because the balance should only change through
    # deposit(), withdraw(), or add_annual_interest(), where validation is done.
    # If balance could be assigned directly, someone could set it to an invalid
    # value and bypass the minimum-balance and transaction rules.
    #
    # holder_name can safely stay public because changing an account holder's name
    # does not affect the account's balance or financial rules.
    @property
    def balance(self):
        """Return the account balance."""
        return self.__balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if not BankAccount.is_valid_amount(amount):
            raise ValueError("Deposit amount must be positive")

        self.__balance += amount
        return self.__balance

    def withdraw(self, amount, pin):
        """Withdraw money after verifying the PIN."""
        if not self.__verify_pin(pin):
            raise ValueError("Incorrect PIN")

        if not BankAccount.is_valid_amount(amount):
            raise ValueError("Withdrawal amount must be positive")

        if self.__balance - amount < BankAccount.MIN_BALANCE:
            raise ValueError(
                f"Insufficient funds. Minimum balance "
                f"{BankAccount.MIN_BALANCE} must remain"
            )

        self.__balance -= amount
        return self.__balance

    def __verify_pin(self, pin):
        """Verify the account PIN."""
        return self.__pin == pin

    def change_pin(self, old_pin, new_pin):
        """Change the account PIN after verifying the old PIN."""
        if not self.__verify_pin(old_pin):
            raise ValueError("Incorrect PIN")

        if not isinstance(new_pin, str) or len(new_pin) != 4 or not new_pin.isdigit():
            raise ValueError("PIN must be exactly 4 digits")

        self.__pin = new_pin

    def add_annual_interest(self):
        """Add annual interest to the account balance."""
        interest = self.__balance * BankAccount.interest_rate / 100
        self.__balance += interest
        return interest

    @classmethod
    def get_total_accounts(cls):
        """Return the total number of bank accounts."""
        return cls.total_accounts

    @staticmethod
    def is_valid_amount(amount):
        """Check whether an amount is positive."""
        return isinstance(amount, (int, float)) and amount > 0

    def __str__(self):
        """Return a readable account summary without showing the PIN."""
        return (
            f"Account[{self.account_number}] {self.holder_name} | "
            f"{self._account_type} | Rs.{self.balance:,.2f}"
        )


def main():
    """Demonstrate all BankAccount requirements."""

    print("Bank:", BankAccount.bank_name)

    a1 = BankAccount( 
        "Ravi Kumar",
        "Savings",
        5000,
        "1234"
    )

    a2 = BankAccount(
        "Anita Sharma",
        "Current",
        20000,
        "5678"
    )

    print(a1)
    print(a2)

    print("Total accounts:", BankAccount.get_total_accounts())

    print("Deposit 2000 ->", a1.deposit(2000))

    print("Withdraw 1500 ->", a1.withdraw(1500, "1234"))

    print("Interest added:", a1.add_annual_interest())
    print("Balance now:", a1.balance)

    a1.change_pin("1234", "4321")
    print("PIN changed successfully")

    try:
        a1.withdraw(1000, "1234")
    except ValueError as e:
        print("Blocked (wrong PIN):", e)

    try:
        a1.withdraw(6000, "4321")
    except ValueError as e:
        print("Blocked (below min):", e)

    try:
        a1.deposit(-500)
    except ValueError as e:
        print("Blocked (negative):", e)

    try:
        a1.balance = 999999
    except AttributeError as e:
        print("Blocked (write balance):", e)


if __name__ == "__main__":
    main()